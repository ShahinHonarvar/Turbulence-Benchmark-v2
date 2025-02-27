from itertools import permutations

def palindromes_between_indices(s):
    chars = {c.lower() for c in s[3:8] if c.lower().isalpha()}
    if len(chars) < 6:
        return set()
    palindromes = set()
    for p in permutations(chars, 6):
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes