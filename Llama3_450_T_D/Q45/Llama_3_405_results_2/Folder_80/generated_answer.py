from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:9] if c.isalpha()]
    letters_set = set(letters)
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for perm in permutations(letters_set, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes