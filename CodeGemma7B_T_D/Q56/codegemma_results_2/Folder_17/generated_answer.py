def all_substring_of_size_n(str):
    if len(str) < 37:
        return []
    result = set()
    for i in range(len(str) - 36):
        substring = str[i:i + 37]
        if len(substring) == len(set(substring)):
            result.add(substring)
    return list(result)