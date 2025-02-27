def all_substring_of_size_n(s):
    if len(s) < 20:
        return []
    substrings = set()
    for i in range(len(s) - 19):
        sub = s[i:i + 20]
        if len(set(sub)) == 20:
            substrings.add(sub)
    return list(substrings)