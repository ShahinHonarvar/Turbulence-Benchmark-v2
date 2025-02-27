import re

def palindrome_of_length_n(string, target_length=43):
    english_letters = re.findall('[a-zA-Z]', string)
    if len(english_letters) < target_length:
        return set()
    palindromes = set()
    for i in range(len(english_letters) - target_length + 1):
        palindrome = english_letters[i:i + target_length]
        if palindrome == palindrome[::-1]:
            palindromes.add(''.join(palindrome))
    return palindromes