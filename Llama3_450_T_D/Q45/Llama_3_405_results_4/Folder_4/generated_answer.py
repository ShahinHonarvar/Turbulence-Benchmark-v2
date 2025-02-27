import itertools

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[3:10] if c.isalpha()]
    if len(chars) < 7:
        return set()
    palindromes = set()
    for r in range(7, len(chars) + 1):
        for perm in itertools.permutations(chars, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes