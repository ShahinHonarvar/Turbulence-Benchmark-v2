def all_substring_of_size_n(s):
    if len(s) < 28:
        return []
    substrings = set()
    for i in range(len(s) - 28 + 1):
        substr = ''.join(sorted(s[i:i + 28]))
        substrings.add(substr)
    return list(substrings)