import re

def palindromes_of_specific_lengths(s):
    s = s.lower()[21:63]
    palindromes = set()
    for i in range(len(s) - 21):
        for j in range(22, 34):
            if i + j <= len(s):
                palindrome = s[i:i + j]
                if palindrome == palindrome[::-1] and re.match('^[a-zA-Z]*$', palindrome):
                    palindromes.add(palindrome)
    return palindromes