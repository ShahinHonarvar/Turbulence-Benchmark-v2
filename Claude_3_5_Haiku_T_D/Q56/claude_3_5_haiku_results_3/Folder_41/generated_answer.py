def all_substring_of_size_n(s):
    if len(s) < 74:
        return []
    result = set()
    for i in range(len(s) - 73):
        substr = s[i:i + 74]
        if len(set(substr)) == 74:
            result.add(substr)
    return list(result)