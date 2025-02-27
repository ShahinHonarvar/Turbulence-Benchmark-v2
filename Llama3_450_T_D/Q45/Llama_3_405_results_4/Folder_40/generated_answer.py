from itertools import permutations

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[4:10] if c.isalpha()]
    if len(chars) < 7:
        return set()
    palindromes = set()
    for r in range(7, len(chars) + 1):
        for perm in permutations(chars, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes