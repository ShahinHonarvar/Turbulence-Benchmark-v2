import itertools

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[2:7] if c.isalpha()]
    unique_chars = list(set(chars))
    palindromes = set()
    for r in range(2, len(unique_chars) + 1):
        for perm in itertools.permutations(unique_chars, r):
            palindrome = ''.join(perm) + ''.join(perm)[::-1]
            if len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes