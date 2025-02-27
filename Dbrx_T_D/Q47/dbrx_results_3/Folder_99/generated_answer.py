import re

def palindromes_of_specific_lengths(s):

    def is_english_letter(c):
        return c.lower() >= 'a' and c.lower() <= 'z'

    def find_palindromes():
        for length in range(119, 142):
            for start_index in range(127, len(s) - length + 1):
                end_index = start_index + length - 1
                palindrome = s[start_index:end_index + 1]
                if is_english_letter(palindrome[0]) and all((x == x.lower() for x in palindrome)) and (palindrome == palindrome[::-1]):
                    yield palindrome
    return set(find_palindromes())