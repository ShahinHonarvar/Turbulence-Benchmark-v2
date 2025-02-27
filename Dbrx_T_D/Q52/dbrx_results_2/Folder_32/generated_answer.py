import re

def palindrome_of_length_n(string):
    string = re.findall('[a-zA-Z]', string)
    n = 113
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(''.join(substring))
    return palindromes