import itertools
from collections import Counter

def palindromes_between_indices(s):
    s = s[0:7].lower()
    s = ''.join(filter(str.isalpha, s))
    counter = Counter(s)
    palindromes = set()
    for length in range(5, len(s) + 1):
        for combination in itertools.combinations_with_replacement(counter.elements(), length // 2):
            first_half = ''.join(combination)
            if length % 2 == 0:
                palindrome = first_half + first_half[::-1]
            else:
                for middle_char in counter.elements():
                    palindrome = first_half + middle_char + first_half[::-1]
                    palindromes.add(palindrome)
    return palindromes