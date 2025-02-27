import re

def palindromes_between_indices(text):
    text = re.sub('[^A-Za-z0-9]+', '', text)
    return set(re.findall('[A-Za-z0-9]+\x01+[A-Za-z0-9]+', text[5:9]))