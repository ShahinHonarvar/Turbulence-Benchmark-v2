def filter_chars(text):
    filtered = ''.join([c for c in text if c not in ''.join([ch for ch in text[44:68] if ch > 'W' and ch < 'x'])])
    return filtered