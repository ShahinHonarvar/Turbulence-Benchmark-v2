def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 24):
        substring = s[i:i + 25]
        if len(set(substring)) == 25:
            substrings.add(substring)
    return list(substrings)