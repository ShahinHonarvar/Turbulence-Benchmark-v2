def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s) - 46):
        subs = s[i:i + 47]
        if subs == subs[::-1] and subs.isalpha():
            res.add(subs)
    return res