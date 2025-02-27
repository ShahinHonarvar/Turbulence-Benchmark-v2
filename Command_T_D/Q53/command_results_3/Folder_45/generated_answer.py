import re

def palindrome_of_length_at_least_n(s):
    return set(re.findall('(?i)(\\w){47}(?i\\1)', s))