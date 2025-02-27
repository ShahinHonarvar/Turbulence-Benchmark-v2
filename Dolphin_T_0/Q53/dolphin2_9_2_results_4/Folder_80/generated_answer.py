import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    pattern = re.compile('([a-z]{30,})(?=.*\\\\1)')
    palindromes = set(pattern.findall(s))
    palindromes.update((word for word in palindromes if word[::-1] in s))
    return palindromes