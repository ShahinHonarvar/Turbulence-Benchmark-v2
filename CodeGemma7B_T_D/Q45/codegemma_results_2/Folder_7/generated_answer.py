from itertools import permutations

def palindromes_between_indices(s):
    left, right = (1, 9)
    english_letters = ''.join((char for char in s[left:right + 1] if char.isalpha())).lower()
    if not english_letters:
        return set()
    palindromes = set()
    for perm in permutations(english_letters):
        palindrome = ''.join(perm)
        if len(palindrome) >= 7:
            palindromes.add(palindrome)
    return palindromes