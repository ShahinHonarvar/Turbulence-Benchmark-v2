from itertools import permutations, chain

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    valid_indices = range(2, 9)
    letters = [c for c in s if c.isalpha()]
    letters = [c for i, c in enumerate(letters) if 2 <= i < 9]
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for subset in chain.from_iterable(permutations(letters, length)):
            if is_palindrome(''.join(subset)):
                palindromes.add(''.join(subset))
    return palindromes