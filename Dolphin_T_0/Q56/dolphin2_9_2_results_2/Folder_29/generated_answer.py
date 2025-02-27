def all_substring_of_size_n(s):
    if len(s) < 95:
        return []
    substrings = set()
    for i in range(len(s) - 94):
        sub = s[i:i + 95]
        if len(set(sub)) == 95:
            substrings.add(sub)
    return list(substrings)