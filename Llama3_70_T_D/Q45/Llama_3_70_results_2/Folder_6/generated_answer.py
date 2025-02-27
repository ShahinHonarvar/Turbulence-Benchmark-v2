from itertools import combinations, permutations
import re

def palindromes_between_indices(s):
    s = s[:8].lower()
    letters = re.findall('[a-z]', s)
    palindromes_set = set()
    for r in range(4, len(letters) + 1):
        for combo in combinations(letters, r):
            for perm in permutations(combo):
                if perm == perm[::-1]:
                    palindrome = ''.join(perm)
                    if palindrome not in palindromes_set:
                        palindromes_set.add(palindrome)
    return palindromes_set