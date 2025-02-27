def all_substring_of_size_n(s):
    result = []
    if len(s) < 98:
        return result
    for i in range(len(s) - 97):
        substring = s[i:i + 98]
        if len(set(substring)) == 98:
            result.append(substring)
    return result