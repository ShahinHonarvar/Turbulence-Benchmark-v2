def all_substring_of_size_n(s):
    if len(s) < 36:
        return []
    result = []
    for i in range(len(s) - 35):
        substring = s[i:i + 36]
        if len(set(substring)) == 36:
            result.append(substring)
    return result