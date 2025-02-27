import re

def palindrome_of_length_at_least_n(string):
    pali = re.findall('([a-zA-Z]{83,})', string, flags=re.MULTILINE | re.IGNORECASE).set()
    return pali