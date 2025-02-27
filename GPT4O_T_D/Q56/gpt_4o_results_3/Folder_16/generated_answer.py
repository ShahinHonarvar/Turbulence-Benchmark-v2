def all_substring_of_size_n(s):
    if len(s) < 124:
        return []
    result = []
    for i in range(len(s) - 123):
        substring = s[i:i + 124]
        if len(substring) == 124 and len(set(substring)) == 124:
            result.append(substring)
    return result