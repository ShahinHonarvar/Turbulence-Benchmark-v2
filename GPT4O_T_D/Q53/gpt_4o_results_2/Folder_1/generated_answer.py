import re

def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = re.sub('[^a-zA-Z]', '', s).lower()
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 29, n + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes