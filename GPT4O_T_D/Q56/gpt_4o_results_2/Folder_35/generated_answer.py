def all_substring_of_size_n(s):
    substrings = set()
    length = len(s)
    for i in range(length - 26):
        substring = s[i:i + 27]
        if len(substring) == 27 and len(set(substring)) == 27:
            substrings.add(substring)
    return list(substrings)