def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 2):
        if len(set(s[i:i + 3])) == 3:
            substrings.add(s[i:i + 3])
    return list(substrings)