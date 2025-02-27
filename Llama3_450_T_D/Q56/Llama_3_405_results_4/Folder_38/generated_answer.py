def all_substring_of_size_n(string):
    result = set()
    for i in range(len(string) - 34):
        substring = string[i:i + 35]
        if len(set(substring)) == 35:
            result.add(substring)
    return list(result)