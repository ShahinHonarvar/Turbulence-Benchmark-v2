from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:8].lower()
    s = ''.join(filter(str.isalpha, s))
    counter = Counter(s)
    palindromes = set()
    for r in range(len(s) // 2 + 1):
        for perm in permutations(s, r):
            first_half = ''.join(perm)
            second_half = first_half[::-1]
            middle = ''.join(perm[:len(s) - 2 * len(first_half)])
            palindrome = first_half + middle + second_half
            if len(palindrome) >= 6 and all((counter[c] >= palindrome.count(c) for c in set(palindrome))):
                palindromes.add(palindrome)
    return palindromes