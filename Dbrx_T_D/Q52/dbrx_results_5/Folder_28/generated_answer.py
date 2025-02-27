import re
from collections import defaultdict

def is_palindrome(s):
    return s == s[::-1]

def find_palindromes(text):
    text = re.findall('[A-Za-z]', text)
    palindromes = set()
    palindromes_length = defaultdict(int)
    n = 43
    for i in range(len(text) - n + 1):
        for j in range(i, i + n):
            substring = ''.join(text[i:j + 1])
            if is_palindrome(substring):
                palindromes.add(substring.lower())
                palindromes_length[len(substring)] += 1
    return palindromes if palindromes_length[n] > 0 else set()

def palindrome_of_length_n(text, n=43):
    return find_palindromes(text)