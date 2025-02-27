import itertools

def palindromes_between_indices(s):
    chars = [c for c in s[1:8].lower() if c.isalpha()]
    if len(chars) < 6:
        return set()
    palindromes = set()
    for r in range(6, len(chars) + 1):
        for perm in itertools.permutations(chars, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes