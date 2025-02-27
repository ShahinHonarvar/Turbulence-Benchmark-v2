import re
from itertools import product

def palindrome_of_length_n(s):
    Sym = set((l + u for l, u in product('abcdefghijklmnopqrstuvwxyz', repeat=2)))
    ans = set()
    for i in range(48):
        p = s[i:]
        for r in [p, p[::-1]]:
            if r in Sym:
                ans.add(r)
    return ans