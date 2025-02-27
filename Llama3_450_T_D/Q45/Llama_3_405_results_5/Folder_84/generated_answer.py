from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10]
    letters = [char.lower() for char in s if char.isalpha()]
    letters_set = set(letters)
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in permutations(letters_set, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes