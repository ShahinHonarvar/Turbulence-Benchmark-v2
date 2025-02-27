def all_substring_of_size_n(s):
    length, n = (len(s), 89)
    if length < n:
        return []
    substrings = set()
    for i in range(length - n + 1):
        sub = s[i:i + n]
        if len(set(sub)) == n:
            substrings.add(sub)
    return list(substrings)