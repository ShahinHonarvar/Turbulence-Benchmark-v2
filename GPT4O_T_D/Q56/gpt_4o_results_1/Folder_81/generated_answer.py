def all_substring_of_size_n(s):
    if len(s) < 98:
        return []
    result = set()
    for i in range(len(s) - 97):
        substr = s[i:i + 98]
        if len(set(substr)) == 98:
            result.add(substr)
    return list(result)