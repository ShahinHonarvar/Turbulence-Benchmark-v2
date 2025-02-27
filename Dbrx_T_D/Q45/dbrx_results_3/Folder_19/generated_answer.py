import re

def palindromes_between_indices(s):
    english_letters = re.findall('[a-zA-Z]', s[0:7])
    if len(english_letters) < 7:
        return set()
    palindromes = set()
    for i in range(len(english_letters), 6, -1):
        for j in range(0, len(english_letters) - i + 1):
            palindrome = ''.join(english_letters[j:j + i])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome.lower())
    return palindromes