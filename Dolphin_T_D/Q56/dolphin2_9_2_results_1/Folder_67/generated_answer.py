def all_substring_of_size_n(s):
    result = []
    if len(s) != 43:
        return result
    for i in range(len(s)):
        for j in range(i + 43, len(s) + 1):
            if len(set(s[i:j])) == 43:
                result.append(s[i:j])
    return result