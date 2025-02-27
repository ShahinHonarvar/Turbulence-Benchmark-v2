import re

def palindrome_of_length_at_least_n(s):
    final = set()
    pattern = re.compile('([a-z])\\\\1{13,}')
    for word in pattern.findall(s):
        final.add(word.lower())
    return final