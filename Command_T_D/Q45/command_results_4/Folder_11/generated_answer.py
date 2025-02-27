import re

def palindromes_between_indices(text):
    text = re.sub('[^a-z0-9]+', '', text)
    return set(re.findall('(?<=.)(.*?)(?=.)', text[3:-7], flags=re.I))