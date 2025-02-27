import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[:5] if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combo in itertools.combinations(letters, length):
            palindrome = ''.join(combo)
            if palindrome.lower() == palindrome.lower()[::-1]:
                palindromes.add(palindrome.lower())
    return palindromes