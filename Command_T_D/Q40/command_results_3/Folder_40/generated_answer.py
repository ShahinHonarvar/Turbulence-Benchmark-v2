import re

def return_n_smallest_chars(s):
    return re.findall('<c>([a-z])</c>', s, flags=re.I)[0][::-1]