from collections import defaultdict
    import re

def palindromes_between_indices(s):
    eng_letters = {chr(i).lower() for i in range(ord('a'), ord('z') + 1)}
    letters = {c.lower() for c in s[:4]} & eng_letters
    letters.update({c.lower() for c in s[10:]} & eng_letters)
    palindromes = set()
    for i in range(5, 10):
        for j in range(10 - i):
            substr = s[4 + i:4 + i + j + 1]
            substr = ''.join((c.lower() for c in substr if c.lower() in eng_letters))
            if len(substr) == 0:
                continue
            if len(substr) % 2 == 1:
                substr = substr[:-1]
                j -= 1
            if len(substr) == 0:
                continue
            d = defaultdict(int)
            for c in substr:
                d[c] += 1
            if any((c.count > 1 for c in d.values())):
                continue
            palindromes.add(substr + substr[::-1])
    return palindromes