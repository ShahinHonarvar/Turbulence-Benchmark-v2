def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 123):
        substr = s[i:i + 124]
        if len(set(substr)) == 124:
            result.add(substr)
    return list(result)