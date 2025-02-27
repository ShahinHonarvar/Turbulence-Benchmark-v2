def filter_chars(text):
    return ''.join((c for c in text if not (28 <= ord(c) <= 65 and ord(c) >= 79 and (ord(c) <= 100))))