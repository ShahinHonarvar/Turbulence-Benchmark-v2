import re

def palindrome_of_length_at_least_n(s: str) -> set:
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 25):
        sub = s[i:i + 26]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes