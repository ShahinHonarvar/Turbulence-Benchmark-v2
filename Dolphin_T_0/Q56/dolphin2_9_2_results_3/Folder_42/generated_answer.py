def all_substring_of_size_n(s):
    length = 45
    substrings = set([])
    for i in range(len(s) - length + 1):
        sub = s[i:i + length]
        if len(set(sub)) == length:
            substrings.add(sub)
    return list(substrings)