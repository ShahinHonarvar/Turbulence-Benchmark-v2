import re

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    pattern = re.compile('(.)(?=\\\\1)(.)(?=\\\\2)(.)(?=\\\\3)(.)(?=\\\\4)(.)(?=\\\\5)')
    return set(pattern.findall(text))