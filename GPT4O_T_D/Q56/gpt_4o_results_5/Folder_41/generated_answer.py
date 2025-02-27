def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 73):
        sub = s[i:i + 74]
        if len(set(sub)) == 74:
            substrings.add(sub)
    return list(substrings)