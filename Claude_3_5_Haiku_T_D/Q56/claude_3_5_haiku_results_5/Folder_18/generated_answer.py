def all_substring_of_size_n(s):
    if len(s) < 63:
        return []
    result = []
    for i in range(len(s) - 62):
        substring = s[i:i + 63]
        if len(set(substring)) == 63:
            result.append(substring)
    return list(set(result))