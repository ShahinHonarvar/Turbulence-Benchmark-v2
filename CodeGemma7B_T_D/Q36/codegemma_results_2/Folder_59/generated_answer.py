def filter_chars(txt):
    return ''.join([i for i in txt[:3] + txt[8:] if i not in txt[3:8]])