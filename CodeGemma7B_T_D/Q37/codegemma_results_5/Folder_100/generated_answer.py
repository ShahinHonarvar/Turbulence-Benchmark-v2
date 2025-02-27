import string

def filter_chars(txt):
    for i, char in enumerate(txt):
        if i >= 88 and i <= 90 and (char >= 'J') and (char <= 'Q'):
            txt = txt[:i] + txt[i + 1:]
    return txt