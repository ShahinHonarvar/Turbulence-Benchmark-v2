import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[:4].lower() if c.isalpha()]
    palindromes = set()
    for r in range(2, len(letters) + 1):
        for p in itertools.permutations(letters, r):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1] and len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes