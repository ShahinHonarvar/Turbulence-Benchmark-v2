import itertools

def palindromes_between_indices(string):
    letters = [c for c in string[1:7] if c.isalpha()]
    palindromes = set()
    for c in itertools.permutations(letters):
        palindrome = ''.join(c).lower()
        if len(palindrome) >= 6:
            palindromes.add(palindrome)
    return palindromes