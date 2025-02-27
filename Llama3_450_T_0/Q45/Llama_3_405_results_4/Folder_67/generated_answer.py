import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[2:7] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for combo in itertools.permutations(letters, r):
            palindrome = ''.join(combo)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes