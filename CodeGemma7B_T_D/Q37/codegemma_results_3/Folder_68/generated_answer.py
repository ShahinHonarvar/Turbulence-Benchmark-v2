def filter_chars(text):
    filtered_text = ''.join((c for c in text if c not in text[7:10] or not (c >= '6' and c <= 'w')))
    return filtered_text