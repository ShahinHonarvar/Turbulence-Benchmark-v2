import re

def palindromes_of_specific_lengths(s):
    s = re.sub('[^a-zA-Z]', '', s.lower())
    return {palindrome for length in range(50, 53) for i in range(17, 73 - length) for palindrome in {s[i:i + length]} if palindrome == palindrome[::-1]}