def all_substring_of_size_n(s):
    n = len(s)
    substrings = set()
    for i in range(n):
        for j in range(i + 55, n + 1):
            sub = s[i:j]
            if len(set(sub)) == len(sub):
                substrings.add(sub)
    return list(substrings)