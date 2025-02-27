def all_substring_of_size_n(s):
    substrings = set()
    n = len(s)
    for i in range(n - 26):
        substring = s[i:i + 27]
        if len(set(substring)) == 27:
            substrings.add(substring)
    return list(substrings)