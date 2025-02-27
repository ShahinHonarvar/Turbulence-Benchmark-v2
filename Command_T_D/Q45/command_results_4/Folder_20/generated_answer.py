import re

def palindromes_between_indices(s):
    for m in re.finditer('(.*?[a-z])(.*?[A-Z])(.*?[a-z])(.*?[A-Z])(.*?[a-z])(.*?[A-Z])(.*?[a-z])', s):
        yield m.group()