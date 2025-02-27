def all_substring_of_size_n(str):
    result = set()
    for i in range(len(str) - 51):
        for j in range(i + 1, len(str)):
            substring = str[i:j + 1]
            if len(substring) == len(set(substring)):
                result.add(substring)
    return list(result)