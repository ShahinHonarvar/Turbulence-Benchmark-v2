def all_substring_of_size_n(s):
    n = 92
    set_s = set()
    for i in range(len(s) - n + 1):
        substrings = s[i:i + n]
        if len(set(substrings)) == n:
            set_s.add(substrings)
    return list(set_s)