def all_substring_of_size_n(string):
    if len(string) < 92:
        return []
    result = set()
    for i in range(len(string) - 91):
        substring = string[i:i + 92]
        if len(set(substring)) == 92:
            result.add(substring)
    return list(result)