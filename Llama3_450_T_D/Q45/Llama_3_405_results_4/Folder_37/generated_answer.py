import itertools
from collections import Counter

def palindromes_between_indices(s):
    s = s[1:5].lower()
    s = ''.join(filter(str.isalpha, s))
    counter = Counter(s)
    palindromes = set()
    for length in range(5, len(s) + 1):
        for combination in itertools.combinations_with_replacement(counter.elements(), length // 2):
            first_half = ''.join(combination)
            palindrome = first_half + first_half[::-1]
            if length % 2 != 0:
                for letter in counter.elements():
                    palindromes.add(palindrome + letter)
            else:
                palindromes.add(palindrome)
    return palindromes