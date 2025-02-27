def all_substring_of_size_n(string):
    result = set()
    for i in range(len(string) - 42):
        substring = string[i:i + 43]
        result.add(substring)
    return list(result)