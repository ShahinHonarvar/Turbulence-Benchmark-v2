def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 22):
        sub = s[i:i + 23]
        if len(set(sub)) == 23:
            substrings.add(sub)
    return list(substrings)