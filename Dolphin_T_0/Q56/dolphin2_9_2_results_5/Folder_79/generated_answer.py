def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 60):
        sub = s[i:i + 61]
        if len(set(sub)) == 61:
            substrings.add(sub)
    return list(substrings)