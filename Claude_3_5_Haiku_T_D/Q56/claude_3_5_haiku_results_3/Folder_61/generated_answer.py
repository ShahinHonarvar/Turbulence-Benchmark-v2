def all_substring_of_size_n(s):
    if len(s) < 39:
        return []
    result = set()
    for i in range(len(s) - 38):
        substr = s[i:i + 39]
        if len(set(substr)) == 39:
            result.add(substr)
    return list(result)