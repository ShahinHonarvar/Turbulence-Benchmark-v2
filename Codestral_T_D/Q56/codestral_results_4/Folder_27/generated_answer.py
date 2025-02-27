def all_substring_of_size_n(s):
    n = 57
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if j - i == n and len(set(s[i:j])) == n:
                substrings.add(s[i:j])
    return list(substrings)