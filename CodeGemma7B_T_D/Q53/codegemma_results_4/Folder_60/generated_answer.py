import re

def palindrome_of_length_at_least_n(text):
    palindromes = set()
    text = text.lower()
    regex = re.compile('(?<![a-z])([a-z])\\\\1{78,}(?<!\\\\1|[a-z])')
    iterator = regex.finditer(text)
    for match in iterator:
        palindrome = match.group(1)
        palindromes.add(palindrome)
    return palindromes