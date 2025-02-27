from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c.lower() for c in text[3:9] if c.isalpha()))
    if not letters:
        return set()
    palindromes = set()
    for p in permutations(letters):
        palindrome = ''.join(p)
        palindromes.add(palindrome)
    return palindromes