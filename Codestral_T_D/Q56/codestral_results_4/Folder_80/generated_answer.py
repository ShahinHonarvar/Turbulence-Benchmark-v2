def all_substring_of_size_n(s):
    n = 31
    substrings = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if len(set(sub)) == len(sub):
            substrings.add(sub)
    return list(substrings)