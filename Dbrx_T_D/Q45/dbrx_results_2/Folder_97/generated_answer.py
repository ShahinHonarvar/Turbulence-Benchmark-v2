from collections import defaultdict
import re

def palindromes_between_indices(s):
    s = s.lower()
    chars = defaultdict(int)
    for i in range(5):
        chars[s[i]] += 1
    palindromes = set()
    for i in range(5):
        for j in range(i, 5):
            for k in range(i, j + 1):
                chars[s[k]] -= 1
                if chars[s[k]] == 0:
                    del chars[s[k]]
                if not chars:
                    palindromes.add(s[i:j + 1])
                chars[s[k]] += 1
    return palindromes