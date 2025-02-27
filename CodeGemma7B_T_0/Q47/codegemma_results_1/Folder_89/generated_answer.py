import re

def palindromes_of_specific_lengths(text):
    text = text.lower()
    pattern = re.compile('(?<=[\\\\w]{18})[\\\\w]{12,14}(?=\\\\w{14}[\\\\w]{18})')
    return {word for word in re.findall(pattern, text)}