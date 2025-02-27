import re
import string

def palindromes_between_indices(s):
    english_letters = set(string.ascii_letters)
    palindromes = set()
    for i in range(1, 6):
        for j in range(i + 1, 7):
            substring = s[i:j + 1]
            letters = set(re.findall('[%s]' % '|'.join(english_letters), substring))
            if len(letters) < 6:
                continue
            palindrome = ''
            while letters:
                letter = letters.pop()
                palindrome += letter
                if len(palindrome) >= 7 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome.lower())
    return palindromes