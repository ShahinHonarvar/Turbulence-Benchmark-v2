import re

def palindromes_between_indices(s):
    english_letters = re.findall('[a-zA-Z]', s[8:10])
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i, len(english_letters)):
            palindrome = ''.join(english_letters[i:j + 1])
            if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome.lower())
    return palindromes