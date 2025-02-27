def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 1):
        substr = s[i:i + 2]
        if len(set(substr)) == 2:
            result.add(substr)
    return list(result)