def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 23):
        sub = s[i:i + 24]
        if len(set(sub)) == 24:
            substrings.add(sub)
    return list(substrings)