def palindrome_of_length_at_least_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            subs = s[i:j]
            if len(subs) >= 55 and subs == subs[::-1]:
                res.add(subs)
    return res