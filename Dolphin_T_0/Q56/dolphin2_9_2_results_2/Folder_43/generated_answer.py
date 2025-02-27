def all_substring_of_size_n(s):
    if len(s) < 86:
        return []
    substrings = set()
    for i in range(len(s) - 85):
        subs = s[i:i + 86]
        if len(set(subs)) == 86:
            substrings.add(subs)
    return list(substrings)