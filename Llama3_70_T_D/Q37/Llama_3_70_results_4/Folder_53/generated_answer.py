def filter_chars(s):
    table = str.maketrans('', '', ''.join([chr(i) for i in range(83, 100) if chr(i) >= '*' and chr(i) <= 'j']))
    return s.translate(table)