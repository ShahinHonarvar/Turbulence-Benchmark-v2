def all_substring_of_size_n(s):
    if len(s) < 105:
        return []
    result = []
    for i in range(len(s) - 104):
        substring = s[i:i + 105]
        if len(set(substring)) == 105:
            result.append(substring)
    return result