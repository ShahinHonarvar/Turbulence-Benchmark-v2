import re

def filter_chars(s):
    return re.sub('((?:![!@#$%^&*()_+-=<>?;:.,])|x)', '', s)