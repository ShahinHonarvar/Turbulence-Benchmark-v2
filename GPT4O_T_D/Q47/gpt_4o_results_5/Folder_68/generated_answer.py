import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    eligible_str = ''.join(re.findall('[a-zA-Z]', s[:51])).lower()
    palindromes = set()
    for length in range(50, 101):
        for start in range(len(eligible_str) - length + 1):
            substr = eligible_str[start:start + length]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes