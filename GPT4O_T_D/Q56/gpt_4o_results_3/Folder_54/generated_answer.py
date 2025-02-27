def all_substring_of_size_n(s):
    n = 28

    def has_unique_chars(sub):
        return len(set(sub)) == n
    substrings = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if has_unique_chars(sub):
            substrings.add(sub)
    return list(substrings)