import re

def palindrome_of_length_n(string, n=475):
    english_letters = re.findall('[a-zA-Z]', string)
    palindromes = set()
    if len(english_letters) < n:
        return palindromes
    for i in range(len(english_letters) - n + 1):
        candidate = english_letters[i:i + n]
        if english_letters[i:i + n] == english_letters[i + n - 1:i - 1:-1]:
            palindromes.add(''.join(candidate))
    return palindromes