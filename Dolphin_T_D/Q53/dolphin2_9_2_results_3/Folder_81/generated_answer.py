def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    res = set()
    for i in range(len(s)):
        for j in range(i + 32, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                res.add(s[i:j + 1])
    return res