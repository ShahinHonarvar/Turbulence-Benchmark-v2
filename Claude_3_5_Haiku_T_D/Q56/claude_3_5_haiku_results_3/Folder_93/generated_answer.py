def all_substring_of_size_n(s):
    if len(s) < 54:
        return []
    result = set()
    for i in range(len(s) - 53):
        substr = s[i:i + 54]
        if len(set(substr)) == 54:
            result.add(substr)
    return list(result)