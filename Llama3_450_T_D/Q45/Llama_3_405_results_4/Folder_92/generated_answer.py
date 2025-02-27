import itertools
from collections import Counter

def palindromes_between_indices(s):
    s = s[4:8].lower()
    s = ''.join(filter(str.isalpha, s))
    counter = Counter(s)
    palindromes = set()
    for r in range(len(s) // 2 + 1):
        for combo in itertools.combinations_with_replacement(counter.elements(), r):
            palindrome = ''.join(combo) + ''.join(combo[::-1])
            if len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes