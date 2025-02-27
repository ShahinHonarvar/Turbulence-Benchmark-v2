def filter_chars(str):
    return ''.join([c for c in str if not (587 < ord(c) < 648 and c.isalpha())])