import itertools
from collections import Counter

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:7].lower()))
    counter = Counter(s)
    palindromes = set()
    for length in range(4, len(s) + 1, 2):
        for combination in itertools.combinations_with_replacement(counter.elements(), length // 2):
            first_half = ''.join(combination)
            palindrome = first_half + first_half[::-1]
            palindromes.add(palindrome)
    return palindromes