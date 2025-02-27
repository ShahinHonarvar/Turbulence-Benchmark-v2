def filter_chars(s):
    for char in range(39, 87):
        if '!' < char < '}':
            s = ''.join([c for c in s if c != char])
    return s