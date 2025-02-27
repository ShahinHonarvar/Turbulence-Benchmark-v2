def all_substring_of_size_n(s):
    n = 34
    substrings = set()
    for i in range(len(s)):
        if len(s[i:i + n]) == n:
            sub = ''.join(sorted(s[i:i + n]))
            substrings.add(sub)
    return list(substrings)