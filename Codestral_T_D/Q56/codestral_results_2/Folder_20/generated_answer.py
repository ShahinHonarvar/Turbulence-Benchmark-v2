def all_substring_of_size_n(s):
    n = 50
    substrings = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if len(substring) == len(set(substring)):
                substrings.add(substring)
    return list(substrings)