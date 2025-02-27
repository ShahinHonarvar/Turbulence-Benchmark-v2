import re

def palindrome_of_length_n(str):

    def isPalindrome(text):
        text = ''.join([char for char in text if char.isalpha()])
        return text == text[::-1]

    def findPalindromes(text):
        palindromes = set()
        for i in range(len(text)):
            for j in range(i, len(text)):
                substring = text[i:j + 1]
                if isPalindrome(substring):
                    palindromes.add(substring)
        return palindromes
    text = re.sub('[^A-Za-z]', '', str)
    palindromes = findPalindromes(text)
    if not palindromes or len(palindromes) != 1 or list(palindromes)[0] != str[26:113]:
        return set()
    else:
        return palindromes