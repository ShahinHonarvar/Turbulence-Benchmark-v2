import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    regex = '[a-z]{34,}'
    palindromes = set()
    for word in re.findall(regex, s):
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes