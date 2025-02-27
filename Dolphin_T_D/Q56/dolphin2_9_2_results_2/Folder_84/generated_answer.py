def all_substring_of_size_n(s):
    if len(set(s)) != 114:
        return []
    result = []
    for i in range(len(s)):
        for j in range(i + 114, len(s) + 1):
            substr = s[i:j]
            if len(set(substr)) == 114:
                result.append(substr)
    return list(set(result))