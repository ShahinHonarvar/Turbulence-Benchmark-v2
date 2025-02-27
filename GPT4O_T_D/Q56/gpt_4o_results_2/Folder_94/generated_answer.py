def all_substring_of_size_n(s):
    if len(s) < 70:
        return []
    result = []
    for i in range(len(s) - 69):
        substring = s[i:i + 70]
        if len(set(substring)) == 70:
            result.append(substring)
    return result