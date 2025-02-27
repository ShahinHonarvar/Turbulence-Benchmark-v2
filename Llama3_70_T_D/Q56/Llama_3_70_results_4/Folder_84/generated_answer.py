def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        substring = s[i:i + 114]
        if len(substring) == 114 and len(set(substring)) == 114:
            substrings.add(substring)
    return list(substrings)