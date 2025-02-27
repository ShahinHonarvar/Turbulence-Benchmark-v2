import re

def palindromes_of_specific_lengths(input_string):
    English_letters = re.findall('[a-zA-Z]', input_string[40:95])
    palindromes = {palindrome for length in range(45, 52) for index in range(40, len(English_letters) - length + 1) if (palindrome := English_letters[index:index + length]) == palindrome[::-1]}
    return palindromes