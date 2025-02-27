def all_substring_of_size_n(str):
    result = set()
    for i in range(len(str) - 87 + 1):
        substring = str[i:i + 87]
        if len(substring) == len(set(substring)):
            result.add(substring)
    return list(result)