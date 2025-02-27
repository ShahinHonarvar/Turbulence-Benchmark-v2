import re

def palindromes_of_specific_lengths(input_string):
    palindrome_set = set()
    for length in range(50, 101):
        for start_index in range(50 - length + 1, len(input_string) + 1):
            palindrome = input_string[start_index:start_index + length].lower()
            if palindrome and palindrome == palindrome[::-1] and re.fullmatch('[a-z]*', palindrome):
                palindrome_set.add(palindrome)
    return palindrome_set