import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    s = s[26:85].lower()
    s = re.sub('[^a-z]', '', s)
    result = set()
    n = len(s)
    for length in range(30, 47):
        for start in range(n - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring):
                result.add(substring)
    return result