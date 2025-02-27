import re

def palindromes_of_specific_lengths(input_string):
    input_string = input_string[130:296]
    palindromes = set()
    for length in range(103, 159):
        for i in range(len(input_string) - length + 1):
            palindrome = input_string[i:i + length].lower()
            if palindrome == palindrome[::-1] and re.match('^[a-zA-Z]*$', palindrome):
                palindromes.add(palindrome)
    return palindromes