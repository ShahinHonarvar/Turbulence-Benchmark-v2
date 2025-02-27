import re

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    n = 51
    for center in range(len(text)):
        for step in range(n, 0, -1):
            left = center - step
            right = center + step
            palindrome = text[left:right + 1]
            if left >= 0 and right < len(text) and (palindrome == palindrome[::-1]):
                palindromes.add(palindrome)
    return palindromes