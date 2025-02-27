from string import ascii_lowercase
    from itertools import product

def palindromes_between_indices(s):
    english_letters = [c for c in s.lower() if c in ascii_lowercase]
    if len(english_letters) < 4:
        return set()
    palindromes = set()
    for combo in product(english_letters, repeat=4):
        palindrome = ''.join(combo)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes