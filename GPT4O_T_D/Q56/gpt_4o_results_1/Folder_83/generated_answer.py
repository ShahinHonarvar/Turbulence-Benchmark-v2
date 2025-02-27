def all_substring_of_size_n(s):
    if len(s) < 48:
        return []
    result = []
    for i in range(len(s) - 47):
        substring = s[i:i + 48]
        if len(set(substring)) == 48:
            result.append(substring)
    return result