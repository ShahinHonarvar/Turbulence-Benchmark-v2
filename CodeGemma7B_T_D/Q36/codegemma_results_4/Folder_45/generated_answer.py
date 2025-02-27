def filter_chars(s):
    r = []
    for a, b in enumerate(s):
        if a in range(81, 86):
            if ord('!') < ord(b) < ord('s'):
                continue
        r.append(b)
    return ''.join(r)