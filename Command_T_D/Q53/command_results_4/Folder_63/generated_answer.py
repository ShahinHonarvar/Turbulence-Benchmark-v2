import re

def palindrome_of_length_at_least_n(text):
    return re.findall('<(.)?>(?=.)<\\1>', text.lower())