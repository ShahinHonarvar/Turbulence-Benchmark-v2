def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 34):
        if len(set(s[i:i + 35])) == 35:
            substrings.add(s[i:i + 35])
    return list(substrings)