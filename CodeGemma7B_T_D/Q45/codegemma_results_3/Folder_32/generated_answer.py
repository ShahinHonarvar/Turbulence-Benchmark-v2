from itertools import permutations

def palindromes_between_indices(text):
    letters = [c.lower() for c in text[1:8] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        palindrome = ''.join(p)
        if len(palindrome) >= 5:
            palindromes.add(palindrome)
    return palindromes