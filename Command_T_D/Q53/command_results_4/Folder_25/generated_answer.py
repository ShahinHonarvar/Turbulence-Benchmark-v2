import re

def palindrome_of_length_at_least_n(s):
    return re.findall('<(i){38}(?=\\w)', s, flags=re.I)