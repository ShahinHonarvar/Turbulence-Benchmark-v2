import re

def palindromes_between_indices(text):
    text = re.sub('([A-Z])([A-Z])([A-Z])([A-Z])', ' \x01 \x02 \x03 \x04', text)
    return set(re.findall('([A-Z])([A-Z])([A-Z])([A-Z])', text))