import re

def palindromes_between_indices(s):
    english_letters = re.findall('[a-zA-Z]', s[3:7])
    if len(english_letters) < 3:
        return set()
    palindromes = set()
    for i in range(len(english_letters) - 2):
        for j in range(i + 2, len(english_letters)):
            palindrome = ''.join(english_letters[i:j + 1])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome.lower())
    return palindromes