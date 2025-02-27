import re

def filter_chars(s):
    return re.sub('(?i)[A-Z][a-z]82[A-Z][a-z]83[A-Z][a-z]84[A-Z][a-z]85[A-Z][a-z]86', '', s)