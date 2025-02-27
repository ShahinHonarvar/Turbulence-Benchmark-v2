import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = re.sub('[^a-zA-Z]', '', s[23:83])
    palindromes = set()
    for length in range(32, 35):
        for start in range(0, len(s) - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes