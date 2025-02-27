import re

def palindrome_of_length_at_least_n(string):
    return set(re.findall('(?i)(.+?)(?:\\\\1|\\\\2)\\\\3{4,}', string))