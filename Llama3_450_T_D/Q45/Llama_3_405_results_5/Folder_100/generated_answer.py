import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[:6] if c.isalpha()]
    letters = ''.join(letters).lower()
    unique_letters = set(letters)
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for combo in itertools.permutations(unique_letters, r):
            palindrome = ''.join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes