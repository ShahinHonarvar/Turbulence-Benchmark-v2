def filter_chars(text):
    return ''.join((c for c in text if not (63 <= ord(c) <= 84 and c >= 'E' and (c <= '~'))))