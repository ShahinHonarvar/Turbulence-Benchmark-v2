import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('\\\\W+', '', s.lower())
    palindromes = set()
    for i in range(len(s)):
        palindrome = ''
        for j in range(i, len(s)):
            palindrome += s[j]
            if len(palindrome) >= 26 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes