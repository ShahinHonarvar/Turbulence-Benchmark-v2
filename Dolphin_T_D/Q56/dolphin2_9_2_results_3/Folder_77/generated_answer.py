def all_substring_of_size_n(s):
    if len(set(s)) < 144:
        return []
    substrings = set()
    for i in range(len(s) - 143):
        sub = s[i:i + 144]
        if len(set(sub)) == 144:
            substrings.add(sub)
    return list(substrings)