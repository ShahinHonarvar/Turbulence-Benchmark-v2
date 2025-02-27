from itertools import permutations

def palindromes_between_indices(s):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    letters = ''.join(filter(lambda x: x.lower() in english_letters, s[3:7]))
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in permutations(letters, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes