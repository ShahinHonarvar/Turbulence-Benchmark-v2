def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 83):
        sub = s[i:i + 84]
        if len(set(sub)) == len(sub):
            substrings.add(sub)
    return list(substrings)