def palindromes_of_specific_lengths(s):
    if len(s) < 95:
        return set()
    s = s[39:95]
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s_filtered = ''.join((c for c in s if c in allowed_chars))
    results = set()
    length = len(s_filtered)
    s_filtered = s_filtered.lower()
    for start in range(length):
        for end in range(start + 14, min(start + 53, length + 1)):
            substring = s_filtered[start:end]
            if substring == substring[::-1]:
                results.add(substring)
    return results