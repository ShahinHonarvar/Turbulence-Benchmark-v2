from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for length in range(4, 7):
        for start in range(3 - length + 1, 7 - length + 2):
            substring = s[start:start + length].lower()
            if all((letter in english_letters for letter in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes