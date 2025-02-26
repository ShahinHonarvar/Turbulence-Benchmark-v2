def all_substring_of_size_n(string):
    result = set()
    for i in range(len(string) - 23):
        substring = string[i:i + 24]
        if len(set(substring)) == 24:
            result.add(substring)
    return list(result)