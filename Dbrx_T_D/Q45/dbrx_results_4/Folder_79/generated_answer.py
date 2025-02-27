import re
import string

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[1:8])
    palindromes = {palindrome for length in range(3, len(letters) + 1) for palindrome in {''.join(letters[i:i + length]) for i in range(len(letters) - length + 1)} if palindrome == palindrome[::-1]}
    return palindromes