from itertools import groupby

def insert_after_character(text):
    return ''.join((c if c != '9' else c + 'M' for c in text))