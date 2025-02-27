from itertools import permutations

def palindromes_between_indices(text):
    text = text.lower()
    letters = [c for c in text[1:6] if c.isalpha()]
    permutations = list(permutations(letters))
    palindromes = set()
    for perm in permutations:
        palindrome = ''.join(perm)
        if len(palindrome) >= 4:
            palindromes.add(palindrome)
    return palindromes