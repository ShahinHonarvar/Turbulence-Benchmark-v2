from itertools import permutations

def palindromes_between_indices(text):
    letters = sorted([char for char in text[1:7] if char.isalpha()])
    palindromes = set()
    for perm in permutations(letters):
        palindrome = ''.join(perm) + ''.join(reversed(perm))
        if len(palindrome) >= 6:
            palindromes.add(palindrome.lower())
    return palindromes