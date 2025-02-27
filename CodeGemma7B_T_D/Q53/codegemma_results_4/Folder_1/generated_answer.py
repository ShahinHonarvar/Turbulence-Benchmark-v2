def palindrome_of_length_at_least_n(s: str) -> set[str]:
    s = s.lower()
    res = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            t = s[i:j]
            if t == t[::-1] and len(t) >= 29:
                res.add(t)
    return res