from itertools import product

def palindromes_between_indices(s):
    palindromes = set()
    letters = [c for c in s.lower() if c.isalpha() and 1 <= s.index(c) <= 5]
    for indices in product(range(len(letters)), repeat=len(letters)):
        if is_palindrome([letters[i] for i in indices]):
            palindromes.add(''.join((letters[i] for i in indices)))
    return palindromes

def is_palindrome(letters):
    mid = len(letters) // 2
    for i in range(mid):
        if letters[i] != letters[-i - 1]:
            return False
    return True