import re

def palindrome_of_length_at_least_n(text):
    a = set()
    s = re.findall('[a-zA-Z]{92,}', text)
    for elem in s:
        if elem == elem[::-1]:
            a.add(elem.lower())
    return a