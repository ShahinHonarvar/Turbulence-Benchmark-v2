def all_substring_of_size_n(str):
    if len(str) < 110:
        return []
    result = []
    for i in range(len(str) - 110 + 1):
        substring = str[i:i + 110]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result