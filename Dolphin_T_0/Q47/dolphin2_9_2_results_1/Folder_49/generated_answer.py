import re

def palindromes_of_specific_lengths(input_string):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]

    def is_english_alpha(s):
        return re.match('^[a-zA-Z]*$', s) is not None
    input_string = input_string[10:101]
    length = len(input_string)
    palindrome_set = set()
    for start_index in range(length - 9):
        for end_index in range(0, length - 10 + start_index):
            substring = input_string[start_index:end_index + 11]
            for length in range(10, 51):
                if is_palindrome(substring[0:length]) and is_english_alpha(substring[0:length]):
                    palindrome_set.add(substring[0:length])
    return palindrome_set