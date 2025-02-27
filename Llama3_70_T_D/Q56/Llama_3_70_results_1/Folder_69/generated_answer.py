def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 99 + 1):
        substr = s[i:i + 99]
        if len(set(substr)) == 99:
            result.add(substr)
    return list(result)