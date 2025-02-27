def filter_chars(text):
    return ''.join((i for i in text if i not in ' *s0123456789'))