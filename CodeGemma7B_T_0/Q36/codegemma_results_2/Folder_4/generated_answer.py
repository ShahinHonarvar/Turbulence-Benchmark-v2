def filter_chars(text):
    return ''.join([ch for ch in text if (ch < '6' or ch > 'g') or (ch < 'A' or ch > 'Z') or (ch < 'a' or ch > 'z')])