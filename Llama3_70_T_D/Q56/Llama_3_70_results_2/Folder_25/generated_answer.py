def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        substring = s[i:i + 67]
        if len(substring) == 67 and len(set(substring)) == 67:
            substrings.add(substring)
    return list(substrings)