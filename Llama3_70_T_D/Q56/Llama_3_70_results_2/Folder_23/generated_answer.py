def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 41):
        substr = s[i:i + 42]
        if len(set(substr)) == 42:
            result.add(substr)
    return list(result)