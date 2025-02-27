def palindrome_of_length_at_least_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s)):
        for j in range(i + 40, len(s)):
            subs = s[i:j + 1]
            if subs == subs[::-1]:
                res.add(subs)
    return res