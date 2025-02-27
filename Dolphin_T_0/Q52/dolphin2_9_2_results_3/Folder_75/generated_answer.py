import re

def palindrome_of_length_n(input_string):
    palindromes = set()
    input_string = re.sub('\\W+', '', input_string)
    for i in range(len(input_string) - 79):
        substring = input_string[i:i + 80]
        if substring == substring[::-1].lower() and substring.isalpha():
            palindromes.add(substring)
    return palindromes