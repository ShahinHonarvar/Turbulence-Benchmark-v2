def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 35):
        sub = s[i:i + 36]
        if len(set(sub)) == 36:
            substrings.add(sub)
    return list(substrings)