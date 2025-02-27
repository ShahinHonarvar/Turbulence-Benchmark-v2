import itertools

def palindromes_between_indices(s):
    chars = [c for c in s[7:9] if c.isalpha()]
    chars = ''.join(chars).lower()
    palindromes = set()
    for r in range(3, len(chars) + 1):
        for perm in itertools.permutations(chars, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes