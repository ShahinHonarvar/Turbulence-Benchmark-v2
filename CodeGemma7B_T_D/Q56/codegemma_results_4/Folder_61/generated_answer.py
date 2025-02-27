def all_substring_of_size_n(str):
    if len(str) < 39:
        return []
    result = []
    for i in range(len(str) - 38):
        substring = str[i:i + 39]
        if len(set(substring)) == 39:
            result.append(substring)
    return result