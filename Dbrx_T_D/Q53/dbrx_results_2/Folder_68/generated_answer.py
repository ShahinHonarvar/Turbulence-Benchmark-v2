import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 20):
        for j in range(i + 21, len(s), 21):
            if s[i:j] == s[i:j][::-1] and re.match('[a-zA-Z]+', s[i:j]):
                palindromes.add(s[i:j])
    return palindromes