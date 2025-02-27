def filter_chars(s):
    for c in '!' + ''.join((chr(i) for i in range(ord('!') + 1, ord('@')))) + '@':
        s = s.replace(c, '')
    return s