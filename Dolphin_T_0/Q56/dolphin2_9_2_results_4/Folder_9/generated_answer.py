def all_substring_of_size_n(s):
    substrings = set()
    n = len(s)
    for i in range(n - 33):
        sub = s[i:i + 34]
        if len(set(sub)) == len(sub):
            substrings.add(sub)
    return list(substrings) if substrings else []