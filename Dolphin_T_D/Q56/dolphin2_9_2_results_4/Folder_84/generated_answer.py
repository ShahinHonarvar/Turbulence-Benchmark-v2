def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 113):
        sub = s[i:i + 114]
        if len(set(sub)) == 114:
            substrings.add(sub)
    return list(substrings)