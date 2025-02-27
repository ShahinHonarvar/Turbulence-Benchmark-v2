def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s) - 39):
        subs = s[i:i + 40]
        if subs == subs[::-1]:
            if subs.isalpha():
                res.add(subs)
    return res