import re

def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = re.sub('[^a-zA-Z]', '', s).lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 85, length + 1):
            sub = s[i:j]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes