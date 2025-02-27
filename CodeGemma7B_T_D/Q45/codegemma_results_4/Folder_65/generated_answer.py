from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(set(s[0:7].lower())).replace(' ', '')
    result = set()
    for perm in permutations(letters, r=5):
        palindrome = ''.join(perm)
        if palindrome in s[0:7].lower():
            result.add(palindrome)
    return result