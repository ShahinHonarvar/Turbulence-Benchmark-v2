import re

def palindrome_of_length_n(string):
    regex = re.compile('[^A-Za-z]')
    normalized_string = regex.sub('', string)
    lowercased_string = normalized_string.lower()
    palindromes = set()
    for i in range(len(lowercased_string) - 19):
        substring = lowercased_string[i:i + 20]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes