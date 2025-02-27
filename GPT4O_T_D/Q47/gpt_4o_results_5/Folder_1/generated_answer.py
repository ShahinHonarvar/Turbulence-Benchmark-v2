import re

def palindromes_of_specific_lengths(s):
    s = s[15:90]
    s = re.sub('[^a-zA-Z]', '', s).lower()
    found_palindromes = set()

    def is_palindrome(substr):
        return substr == substr[::-1]
    for length in range(40, 73):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring):
                found_palindromes.add(substring)
    return found_palindromes