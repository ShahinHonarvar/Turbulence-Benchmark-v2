import re

def palindrome_of_length_at_least_n(input_string):
    palindrome_set = set()
    input_string = input_string.lower()
    for i in range(len(input_string)):
        for j in range(i + 25, len(input_string)):
            potential_palindrome = input_string[i:j + 1]
            if re.match('^[a-zA-Z]*$', potential_palindrome) is not None and potential_palindrome == potential_palindrome[::-1]:
                palindrome_set.add(potential_palindrome)
    return palindrome_set