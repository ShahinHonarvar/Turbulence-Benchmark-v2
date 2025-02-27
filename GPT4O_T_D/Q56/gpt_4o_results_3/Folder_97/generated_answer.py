def all_substring_of_size_n(s):
    if len(s) < 142:
        return []
    substrings = set()
    for i in range(len(s) - 141):
        substr = s[i:i + 142]
        if len(set(substr)) == 142:
            substrings.add(substr)
    return list(substrings)