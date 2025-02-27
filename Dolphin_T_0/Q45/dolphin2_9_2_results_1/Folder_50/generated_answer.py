def palindromes_between_indices(s):
    s = s[4:9]
    s = ''.join([c for c in s if c.isalpha()])
    s = s.lower()
    if len(s) < 5:
        return set()
    return {s[i:j] for i in range(len(s)) for j in range(i + 5, len(s) + 1) if s[i:j] == s[i:j][::-1]}