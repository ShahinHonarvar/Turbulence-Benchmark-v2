import re

def palindromes_of_specific_lengths(s):
    s = s[100:301]
    s = re.sub('[^a-zA-Z]', '', s).lower()

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    length = len(s)
    for l in range(50, 101):
        for i in range(length - l + 1):
            sub = s[i:i + l]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes