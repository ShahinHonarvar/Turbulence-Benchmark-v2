def all_substring_of_size_n(s):
    result = []
    if len(set(s)) != len(s):
        return result
    for i in range(len(s)):
        if len(set(s[i:i + 117])) == 117:
            result.append(s[i:i + 117])
    return result