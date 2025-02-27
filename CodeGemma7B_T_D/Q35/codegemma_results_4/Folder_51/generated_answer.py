import re

def remove_repeat_chars(text):
    repeated_chars = set(re.findall('(.)\\\\1+', text[6:9]))
    for char in repeated_chars:
        text = re.sub('(.)\\\\1+', lambda m: m.groups()[0], text, flags=re.DOTALL)
    return text