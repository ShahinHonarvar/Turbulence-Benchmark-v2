from itertools import product

def palindromes_between_indices(s):
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    for i in range(len(s) - 6):
        substring = s[i:i + 7]
        if all((letter.lower() in substring for letter in english_letters)):
            for permutation in product(substring):
                palindrome = ''.join(permutation)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes