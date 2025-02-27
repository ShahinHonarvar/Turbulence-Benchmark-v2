import re

def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[1:9].lower()
    for i in range(3, 5):
        for j in range(len(s) - i + 1):
            palindrome = s[j:j + i]
            if palindrome == palindrome[::-1] and re.match('^[a-zA-Z]*$', palindrome):
                palindromes.add(palindrome)
    return palindromes