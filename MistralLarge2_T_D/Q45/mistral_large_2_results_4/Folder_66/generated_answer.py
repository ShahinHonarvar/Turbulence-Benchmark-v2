from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c for c in s[:6] if c.isalpha())).lower()
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes