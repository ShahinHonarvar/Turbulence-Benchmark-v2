def all_substring_of_size_n(string):
    result = set()
    for i in range(len(string) - 123):
        substring = string[i:i + 124]
        if len(substring) == len(set(substring)):
            result.add(substring)
    return list(result)