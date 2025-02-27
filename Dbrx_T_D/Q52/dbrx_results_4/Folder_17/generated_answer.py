import re

def palindrome_of_length_n(string, length=289):
    string = re.sub('[^a-zA-Z]', '', string.lower())
    n = len(string)
    if n < length:
        return set()
    palindromes = set()
    for i in range(n - length + 1):
        palindrome = string[i:i + length]
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes