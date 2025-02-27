def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 105):
        substr = s[i:i + 106]
        if len(substr) == 106 and len(set(substr)) == 106:
            result.add(substr)
    return list(result)