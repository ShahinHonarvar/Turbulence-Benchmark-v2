import re

def filter_chars(s):
    return re.sub('<[A-Z][A-Z]B[A-Z]C', '', s)