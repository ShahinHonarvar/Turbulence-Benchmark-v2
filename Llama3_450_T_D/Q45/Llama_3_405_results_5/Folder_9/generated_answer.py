from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    s = ''.join(filter(str.isalpha, s))
    counter = Counter(s)
    palindromes = set()
    for r in range(7, len(s) + 1):
        for perm in permutations(s, r):
            perm = ''.join(perm)
            if perm == perm[::-1]:
                palindromes.add(perm)
    for palindrome in list(palindromes):
        counter_copy = counter.copy()
        for char in palindrome:
            counter_copy[char] -= 1
            if counter_copy[char] < 0:
                palindromes.discard(palindrome)
                break
    return palindromes