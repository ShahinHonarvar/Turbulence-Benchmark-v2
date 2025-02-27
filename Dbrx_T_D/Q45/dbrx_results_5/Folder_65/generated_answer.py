from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:7].lower()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    english_letters = [char for char in s if char in english_letters]
    palindromes = set()
    if len(english_letters) >= 2:
        for perm in permutations(english_letters, 2):
            palindrome = perm[0] + perm[1] + perm[0]
            if len(english_letters) >= 3:
                for char in english_letters:
                    palindrome += char
                    palindrome += perm[1]
                    palindrome += char
            if len(palindrome) >= 5 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes