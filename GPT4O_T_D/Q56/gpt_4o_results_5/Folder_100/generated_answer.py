def all_substring_of_size_n(s):
    n = len(s)
    substrings = set()
    for i in range(n - 91):
        substring = s[i:i + 92]
        if len(set(substring)) == 92:
            substrings.add(substring)
    return list(substrings)