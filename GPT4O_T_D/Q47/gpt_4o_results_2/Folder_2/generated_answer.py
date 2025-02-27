import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = s[10:60]
    possible_palindromes = set()
    for length in range(18, 37):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            cleaned_substring = re.sub('[^a-zA-Z]', '', substring).lower()
            if is_palindrome(cleaned_substring) and len(cleaned_substring) == length:
                possible_palindromes.add(substring)
    return possible_palindromes