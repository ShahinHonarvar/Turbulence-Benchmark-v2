def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if len(s[i:i + 23]) == 23:
            if len(set(s[i:i + 23])) == 23:
                substrings.add(s[i:i + 23])
    return list(substrings)