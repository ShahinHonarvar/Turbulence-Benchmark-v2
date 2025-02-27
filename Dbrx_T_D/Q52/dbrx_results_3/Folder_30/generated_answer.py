import re

def palindrome_of_length_n(s):
    n = 94
    s = s.lower()
    english_letters = re.findall('[a-z]', s)
    palindromes = set()
    for i in range(len(english_letters) - n + 1):
        if english_letters[i:i + n] == english_letters[i:i + n][::-1]:
            palindromes.add(''.join(english_letters[i:i + n]))
    return palindromes