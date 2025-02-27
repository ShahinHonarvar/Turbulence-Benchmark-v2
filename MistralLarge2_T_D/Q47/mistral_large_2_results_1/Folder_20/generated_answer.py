import re

def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    sub_str = s[20:75].lower()
    palindromes = set()
    for length in range(36, 43):
        for i in range(len(sub_str) - length + 1):
            sub = sub_str[i:i + length]
            if re.match('^[a-zA-Z]+$', sub) and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes