def all_substring_of_size_n(s):
    n = len(s)
    if n < 130:
        return []
    substrings = set()
    for i in range(n - 129):
        sub = s[i:i + 130]
        if len(set(sub)) == 130:
            substrings.add(sub)
    return list(substrings)