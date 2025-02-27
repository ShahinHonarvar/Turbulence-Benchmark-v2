def all_substring_of_size_n(s):
    if len(s) < 81:
        return []
    result = set()
    for i in range(len(s) - 80):
        substr = s[i:i + 81]
        if len(set(substr)) == 81:
            result.add(substr)
    return list(result)