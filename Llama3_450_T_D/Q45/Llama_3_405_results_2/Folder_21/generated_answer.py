from itertools import permutations

def palindromes_between_indices(s):
    english_letters = [char.lower() for char in s[1:9] if char.isalpha()]
    palindromes = set()
    for r in range(7, len(english_letters) + 1):
        for perm in permutations(english_letters, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes