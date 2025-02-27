import re
from collections import defaultdict

def palindromes_between_indices(s):
    chars = defaultdict(int)
    for i in range(1, 8):
        chars[s[i].lower()] += 1
    palindromes = set()
    for i in range(len(s) - 6):
        for j in range(i + 1, i + 7):
            if s[i].lower() != s[j].lower():
                continue
            count = 0
            for k in range(ord('a'), ord('z') + 1):
                if chars[chr(k)] % 2 == 1:
                    count += 1
                if count > 1:
                    break
            if count == 1:
                palindromes.add(s[i:j + 1].lower())
    return palindromes