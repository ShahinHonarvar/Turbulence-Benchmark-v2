import re

def palindromes_of_specific_lengths(s):
    pattern = re.compile('[a-zA-Z]{104,123}')
    potential_palindromes = pattern.findall(s[119:257])
    palindromes = {palindrome for palindrome in potential_palindromes if palindrome.lower() == palindrome.lower()[::-1]}
    return palindromes