import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[:3].lower() if c.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for combo in itertools.permutations(letters, r):
            palindrome = ''.join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes