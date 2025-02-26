def all_substring_of_size_n(s):
    if len(s) < 37:
        return []
    result = []
    for i in range(len(s) - 36):
        substring = s[i:i + 37]
        if len(set(substring)) == 37:
            result.append(substring)
    return list(dict.fromkeys(result))