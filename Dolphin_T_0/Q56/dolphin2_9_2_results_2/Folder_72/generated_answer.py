def all_substring_of_size_n(string):
    if len(string) < 88:
        return []
    result = set()
    for i in range(0, len(string) - 87):
        substring = string[i:i + 88]
        if len(set(substring)) == 88:
            result.add(substring)
    return list(result)