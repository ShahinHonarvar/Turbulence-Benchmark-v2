import re

def palindrome_of_length_at_least_n(s):
    return re.findall('(?=([A-Z]))\\w{1,138}(?=[A-Z])', s.lower())