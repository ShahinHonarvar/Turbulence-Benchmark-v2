def filter_chars(text):
    return ''.join((c for c in text if not (227 <= len(text) and len(text) <= 235 and (c >= 'D') and (c <= 'u'))))