import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    s = re.sub('[^a-zA-Z]', '', s[23:95]).lower()
    palindromes = set()
    for start in range(len(s)):
        for length in range(17, 56):
            if start + length <= len(s):
                substring = s[start:start + length]
                if is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes