import re
from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = re.findall('[a-zA-Z]', s[6:9])
    if len(english_letters) < 4:
        return set()
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i, len(english_letters)):
            palindrome = ''.join(english_letters[i:j + 1])
            if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome.lower())
    return palindromes