def all_substring_of_size_n(s):
    if len(set(s)) != 27:
        return []
    substrings = set()
    for i in range(len(s) - 26):
        sub = s[i:i + 27]
        if len(set(sub)) == 27:
            substrings.add(sub)
    return list(substrings)