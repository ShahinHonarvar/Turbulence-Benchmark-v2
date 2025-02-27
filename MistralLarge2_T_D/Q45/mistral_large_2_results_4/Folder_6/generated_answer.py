from itertools import permutations

def palindromes_between_indices(s):
    english_letters = [c for c in s[:8] if c.isalpha()]
    palindromes = set()
    for length in range(4, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            palindrome = ''.join(perm).lower()
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes