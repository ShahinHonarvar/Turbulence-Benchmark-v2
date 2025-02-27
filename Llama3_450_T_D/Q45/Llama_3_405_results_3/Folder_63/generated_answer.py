import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:4] if c.isalpha()]
    unique_letters = list(set(letters))
    palindromes = set()
    for r in range(3, len(unique_letters) + 1):
        for perm in itertools.permutations(unique_letters, r):
            palindrome = ''.join(perm) + ''.join(perm[::-1][1:])
            palindromes.add(palindrome)
    return palindromes