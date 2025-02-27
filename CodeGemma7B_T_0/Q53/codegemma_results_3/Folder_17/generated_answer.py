import re

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    pattern = '(?=(%s))' % '|'.join((re.escape(word) for word in re.findall('[a-zA-Z]+', text)))
    return set(re.findall(pattern, text))