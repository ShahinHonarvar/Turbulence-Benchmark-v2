from itertools import permutations

def palindromes_between_indices(s):
    english_letters = [c for c in s[:7] if c.isalpha()]
    palindromes = set()
    for length in range(7, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            palindrome = ''.join(perm)
            if palindrome.lower() == palindrome.lower()[::-1]:
                palindromes.add(palindrome.lower())
    return palindromes