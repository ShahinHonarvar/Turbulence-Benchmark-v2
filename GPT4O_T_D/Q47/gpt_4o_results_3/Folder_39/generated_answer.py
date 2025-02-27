import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    substring = s[31:92]
    letters_only = re.sub('[^a-zA-Z]', '', substring).lower()
    result = set()
    lengths = [50, 51, 52, 53]
    for length in lengths:
        for i in range(len(letters_only) - length + 1):
            potential_palindrome = letters_only[i:i + length]
            if is_palindrome(potential_palindrome):
                result.add(potential_palindrome)
    return result