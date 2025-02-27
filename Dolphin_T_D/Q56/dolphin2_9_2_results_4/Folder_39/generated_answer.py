def all_substring_of_size_n(s):
    n = len(s)
    if n < 94:
        return []
    substrings = set()
    for i in range(n - 93):
        sub = s[i:i + 94]
        if len(set(sub)) == len(sub):
            substrings.add(sub)
    return list(substrings)