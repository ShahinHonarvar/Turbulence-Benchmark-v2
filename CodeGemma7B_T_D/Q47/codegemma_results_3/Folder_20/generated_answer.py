import re

def palindromes_of_specific_lengths(text: str):
    text = text.lower()
    res = set()
    pattern = re.compile('(?<=.{20})([a-z]{36,42})(?=.{34})')
    for m in re.finditer(pattern, text):
        res.add(m.group(1))
    return res