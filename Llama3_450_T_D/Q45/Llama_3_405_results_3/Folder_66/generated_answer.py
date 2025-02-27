import itertools

def palindromes_between_indices(s):
    chars = [c for c in s[:6] if c.isalpha()]
    if len(chars) < 5:
        return set()
    chars = [c.lower() for c in chars]
    palindromes = set()
    for r in range(5, len(chars) + 1):
        for p in itertools.permutations(chars, r):
            if p == p[::-1]:
                palindrome = ''.join(p)
                if len(palindrome) >= 5:
                    palindromes.add(palindrome)
    return palindromes