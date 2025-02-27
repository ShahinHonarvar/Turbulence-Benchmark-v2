def filter_chars(text):
    return ''.join((c for c in text if ord('-') <= ord(c) <= ord('n') or ord(c) < ord('29') or ord(c) > ord('97')))