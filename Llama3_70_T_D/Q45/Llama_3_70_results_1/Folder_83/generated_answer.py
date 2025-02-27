from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:10] if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters, 7):
        palindrome = ''.join(perm) + perm[0]
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes