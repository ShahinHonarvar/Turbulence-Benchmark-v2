import re

def palindromes_of_specific_lengths(s):
    s = s[125:284].lower()
    palindromes = set()
    for length in range(109, 127):
        for i in range(len(s) - length + 1):
            palindrome = s[i:i + length]
            if palindrome == palindrome[::-1]:
                if re.fullmatch('[a-zA-Z]*', palindrome):
                    palindromes.add(palindrome)
    return palindromes