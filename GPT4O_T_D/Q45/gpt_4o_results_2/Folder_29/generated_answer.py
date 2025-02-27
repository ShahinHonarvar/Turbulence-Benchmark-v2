from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:10].lower()
    chars = [c for c in s if c.isalpha()]
    palindromes = set()
    for p in permutations(chars):
        if len(p) >= 6:
            mid = len(p) // 2
            if p[:mid] == p[-mid:][::-1]:
                palindrome = ''.join(p)
                palindromes.add(palindrome)
    return palindromes