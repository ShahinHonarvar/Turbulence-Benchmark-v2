def all_substring_of_size_n(s):
    if len(s) < 48:
        return []
    n = len(set(s))
    if n < 48:
        return []
    substrings = set()
    for i in range(0, len(s)):
        if i + 48 <= len(s):
            substring = s[i:i + 48]
            if len(set(substring)) == 48:
                substrings.add(substring)
    return list(substrings)