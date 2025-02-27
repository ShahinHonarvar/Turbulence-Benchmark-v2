import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:8] if c.isalpha()]
    letters = sorted(set(letters))
    palindromes = set()
    for r in range(2, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                palindrome = ''.join(perm) + ''.join(reversed(perm))
                if len(palindrome) >= 4:
                    palindromes.add(palindrome)
    return palindromes