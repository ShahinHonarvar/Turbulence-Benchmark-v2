import re
import string

def palindrome_of_length_n(s):
    n = 96
    english_letters = string.ascii_letters
    s = s.lower()
    return {palindrome for palindrome in set(re.findall(f'.{{n}}', s)) if palindrome == palindrome[::-1] and all((char in english_letters for char in palindrome))}