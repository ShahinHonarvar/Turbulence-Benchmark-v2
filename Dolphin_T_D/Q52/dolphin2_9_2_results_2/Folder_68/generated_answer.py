def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s) - 75):
        subs = s[i:i + 76]
        if subs == subs[::-1] and subs.isalpha():
            res.add(subs)
    return res