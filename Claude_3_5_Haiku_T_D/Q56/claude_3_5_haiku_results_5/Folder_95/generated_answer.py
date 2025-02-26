def all_substring_of_size_n(s):
    if len(s) < 89:
        return []
    result = []
    for i in range(len(s) - 88):
        substring = s[i:i + 89]
        if len(set(substring)) == 89:
            result.append(substring)
    return list(set(result))