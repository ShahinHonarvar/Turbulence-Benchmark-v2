def all_substring_of_size_n(s):
    n = 28
    substrings = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substr = s[i:j]
            if len(set(substr)) == n:
                substrings.add(substr)
    return list(substrings)