import itertools
    from collections import Counter

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[4:8] if c.isalpha()]
    letter_counts = Counter(letters)
    permutations = set(itertools.permutations(letters))
    palindromes = set()
    for permutation in permutations:
        if permutation == permutation[::-1]:
            palindrome = ''.join(permutation)
            palindromes.add(palindrome)
    palindromes = {p for p in palindromes if len(p) >= 4}
    return palindromes