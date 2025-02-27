from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:9] if c.isalpha()]
    palindromes = set()
    for p in permutations(''.join(letters), 7):
        s = ''.join(p)
        if s.lower() == s[::-1].lower():
            palindromes.add(s)
    return palindromes