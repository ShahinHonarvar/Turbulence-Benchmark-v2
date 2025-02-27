import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[70:141]
    potential_palindromes = re.findall('\\\\b[a-zA-Z]{3,60}\\\\b', substring, re.IGNORECASE)
    result_set = set()
    for palindrome in potential_palindromes:
        lowered_palindrome = palindrome.lower()
        if is_palindrome(lowered_palindrome):
            result_set.add(lowered_palindrome)
    return result_set