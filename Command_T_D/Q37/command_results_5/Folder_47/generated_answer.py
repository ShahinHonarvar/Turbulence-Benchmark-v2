import re

def filter_chars(s):
    return re.sub('(?!:)[a-z]{40}(?<=r)', '', s)