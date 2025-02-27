def all_substring_of_size_n(s):
    if len(s) < 78:
        return []
    substrings = set()
    for i in range(len(s) - 77):
        subs = s[i:i + 78]
        if len(set(subs)) == 78:
            substrings.add(subs)
    return list(substrings)