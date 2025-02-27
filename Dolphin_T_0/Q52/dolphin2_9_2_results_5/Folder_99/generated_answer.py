import re

def palindrome_of_length_n(argument_string):
    palindromes = set()
    argument_string = argument_string.lower()
    for i in range(len(argument_string)):
        for j in range(i + 420, len(argument_string)):
            substring = argument_string[i:j + 1]
            if re.match('^[a-z]*$', substring):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes