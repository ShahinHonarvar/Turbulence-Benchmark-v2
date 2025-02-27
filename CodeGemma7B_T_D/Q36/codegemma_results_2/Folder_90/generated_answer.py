def filter_chars(txt):
    return ''.join((c for c in txt if c not in '\\xef\\xbf\\xbd' and c < 'g' or c > '~'))