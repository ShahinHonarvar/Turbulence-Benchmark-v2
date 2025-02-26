def all_substring_of_size_n(string):
    result = set()
    for i in range(len(string) - 13):
        substring = string[i:i + 14]
        if len(set(substring)) == 14:
            result.add(substring)
    return list(result)