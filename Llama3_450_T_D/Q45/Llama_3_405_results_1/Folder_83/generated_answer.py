import itertools
from collections import Counter

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[2:10] if c.isalpha()]
    char_count = Counter(chars)
    palindromes = set()
    for length in range(7, len(chars) + 1):
        for arrangement in itertools.permutations(chars, length):
            if arrangement == arrangement[::-1]:
                palindrome = ''.join(arrangement)
                palindromes.add(palindrome)
    return palindromes