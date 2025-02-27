def all_substring_of_size_n(s):
    if len(s) < 63:
        return []
    substrings = set()
    for i in range(len(s) - 62):
        sub = s[i:i + 63]
        if len(set(sub)) == len(sub):
            substrings.add(sub)
    return list(substrings)