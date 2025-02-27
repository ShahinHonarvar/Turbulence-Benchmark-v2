def all_substring_of_size_n(string):
    if len(set(string)) != len(string):
        return []
    length = len(string)
    result = set()
    for i in range(length - 42):
        for j in range(i + 43, length + 1):
            substring = string[i:j]
            result.add(substring)
    return list(result)