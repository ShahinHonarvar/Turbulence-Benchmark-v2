def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 36):
        substring = s[i:i + 37]
        if len(set(substring)) == 37:
            substrings.add(substring)
    return list(substrings)