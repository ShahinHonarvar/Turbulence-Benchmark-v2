def all_substring_of_size_n(s):
    if len(s) < 149:
        return []
    result = []
    for i in range(len(s) - 148):
        substring = s[i:i + 149]
        if len(set(substring)) == 149:
            result.append(substring)
    return result