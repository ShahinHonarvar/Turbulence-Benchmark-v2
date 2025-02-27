import re

def palindrome_of_length_at_least_n(s):
    s = re.findall('[a-zA-Z]*', s)
    s = [i.lower() for i in s if len(i) >= 37]
    return {i for i in s if i == i[::-1]}