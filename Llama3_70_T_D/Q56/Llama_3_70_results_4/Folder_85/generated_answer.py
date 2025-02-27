def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 14 + 1):
        substring = s[i:i + 14]
        if len(set(substring)) == 14:
            substrings.add(substring)
    return list(substrings)