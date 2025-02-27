from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:4] if char.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for perm in permutations(letters, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes