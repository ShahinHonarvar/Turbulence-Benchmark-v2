from itertools import permutations

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[1:5] if c.isalpha()]
    palindromes = set()
    for r in range(5, len(chars) + 1):
        for perm in permutations(chars, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes