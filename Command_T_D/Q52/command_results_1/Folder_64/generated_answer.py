import re

def palindrome_of_length_n(s):
    return re.findall('(?i)(?=.*[a-z])(?!.*[a-z])\\w+', s, flags=re.I)