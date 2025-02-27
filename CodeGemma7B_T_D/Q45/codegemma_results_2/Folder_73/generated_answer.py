from itertools import permutations

def palindromes_between_indices(s):
    str1 = s[3:7].lower()
    str2 = ''.join(str1)
    results = []
    for perm in permutations(str1):
        palindrome = ''.join(perm)
        results.append(palindrome)
    return set(results)