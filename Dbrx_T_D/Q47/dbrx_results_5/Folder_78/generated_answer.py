from collections import defaultdict

def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(19, 56):
        for index in range(15, len(s) - length + 2):
            substring = s[index:index + length].lower()
            if all((char in english_letters for char in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes