def all_substring_of_size_n(s):
    if len(set(s)) != len(s):
        return []
    result = []
    for i in range(len(s)):
        for j in range(i + 146, len(s) + 1):
            result.append(s[i:j])
    return result