import re

def palindrome_of_length_at_least_n(s):
    return set(re.findall('(?i)(?=([^aieouAEIOU]{%d})\\1{%d})' % (78, 78), s))