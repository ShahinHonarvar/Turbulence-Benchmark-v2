import re

def palindrome_of_length_at_least_n(str):
    pattern = '[a-zA-Z]{53,}'
    palindromes = set()
    for i in range(len(str)):
        for j in range(i + 53, len(str) + 1):
            substring = str[i:j]
            if re.fullmatch(pattern, substring):
                palindromes.add(substring.lower())
    return palindromes