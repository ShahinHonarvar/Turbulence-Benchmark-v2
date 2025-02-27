def all_substring_of_size_n(s):
    n = len(s)
    substrings = set()
    for i in range(n - 15):
        substring = s[i:i + 16]
        if len(set(substring)) == 16:
            substrings.add(substring)
    return list(substrings)