import re

def palindromes_of_specific_lengths(input_string):
    palindrome_set = set()
    for length in range(18, 74):
        for index in range(15, 95 - length + 1):
            potential_palindrome = input_string[index:index + length]
            if bool(re.match('^[a-zA-Z]*$', potential_palindrome)):
                if potential_palindrome.lower() == potential_palindrome[::-1].lower():
                    palindrome_set.add(potential_palindrome)
    return palindrome_set