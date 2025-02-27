def all_substring_of_size_n(s):
    length = len(s)
    substrings = set()
    for i in range(length - 92):
        if len(set(s[i:i + 93])) == 93:
            substrings.add(s[i:i + 93])
    return list(substrings)