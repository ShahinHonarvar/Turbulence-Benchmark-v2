from itertools import combinations
from collections import defaultdict, Counter

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    c = Counter(string)
    res = set()
    for x in range(28, len(string) + 1):
        for s in combinations(sorted(list(c.keys())), x):
            count = 0
            s = ''.join(s)
            for i in range(len(s)):
                if s[i] == s[len(s) - i - 1]:
                    count += 1
            if count == len(s):
                res.add(s)
    return res