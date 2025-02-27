from itertools import permutations

def palindromes_between_indices(s):
    setOfPalindromes = set()
    letters = ''.join((ch for ch in s[4:10] if ch.isalpha())).lower()
    for p in permutations(letters):
        palindrome = ''.join(p)
        if len(palindrome) >= 6:
            setOfPalindromes.add(palindrome)
    if len(setOfPalindromes) == 0:
        return set()
    return setOfPalindromes