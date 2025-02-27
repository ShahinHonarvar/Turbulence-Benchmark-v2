from collections import defaultdict
import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = re.sub('[^a-zA-Z]', '', s.lower())
    palindromes = set()
    for i in range(39, 95):
        for length in range(14, 53):
            if is_palindrome(s[i:i + length]):
                palindromes.add(s[i:i + length])
    return palindromes