from itertools import product

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    res = set()
    maxlen = len(s)
    for i in range(maxlen):
        for j in range(i + 3, maxlen + 1):
            if s[i:j] == s[j - 1:i - 1:-1]:
                res.add(s[i:j])
    return res