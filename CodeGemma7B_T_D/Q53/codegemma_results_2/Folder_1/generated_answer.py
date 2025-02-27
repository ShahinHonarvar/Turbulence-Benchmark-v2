from collections import defaultdict

def palindrome_of_length_least_n(s):
    s = s.lower()
    count = defaultdict(int)
    for c in s:
        count[c] += 1
    res = set()
    for i in range(len(s)):
        for j in range(i + 32, len(s) + 1):
            tmp = s[i:j]
            tmp2 = tmp[::-1]
            if tmp == tmp2 and count[tmp[0]] >= 2 and (count[tmp[-1]] >= 2):
                res.add(tmp)
    return res