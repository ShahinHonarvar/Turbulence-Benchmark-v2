from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()[:7]
    result = set()
    for p in set(permutations(s)):
        candidate = ''.join(p)
        if candidate == candidate[::-1] and len(candidate) >= 6:
            result.add(candidate)
    return {palindrome for palindrome in result if len(palindrome) >= 6}