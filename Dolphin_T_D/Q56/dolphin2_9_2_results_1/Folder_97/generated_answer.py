def all_substring_of_size_n(s):
    if len(s) < 142:
        return []
    substrings = set()
    for i in range(0, len(s) - 141):
        sub = s[i:i + 142]
        if len(set(sub)) == 142:
            substrings.add(sub)
    return list(substrings)