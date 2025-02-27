def filter_chars(x):
    y = [b for i, b in enumerate(x) if i >= 83 and i <= 99 and (ord(b) >= ord('*')) and (ord(b) <= ord('j'))]
    for a in y:
        x = x.replace(a, '')
    return x