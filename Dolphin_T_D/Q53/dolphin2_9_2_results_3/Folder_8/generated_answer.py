def palindrome_of_length_at_least_n(s):
    res = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            subs = s[i:j]
            if subs == subs[::-1] and len(subs) >= 45:
                res.add(subs)
    return res