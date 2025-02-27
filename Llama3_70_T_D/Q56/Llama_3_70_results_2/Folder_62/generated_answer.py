def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        substring = s[i:i + 32]
        if len(substring) == 32 and len(set(substring)) == 32:
            substrings.add(substring)
    return list(substrings)