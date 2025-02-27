import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    start_index = 124
    end_index = 283
    s = s[start_index:end_index + 1]
    s = re.sub('[^a-zA-Z]', '', s).lower()
    valid_lengths = range(115, 135)
    palindromes = set()
    for length in valid_lengths:
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes