def filter_chars(text):
    to_remove = [i for i in text[29:33] if i > '%' and i < 'a']
    return ''.join([c for c in text if c not in to_remove])