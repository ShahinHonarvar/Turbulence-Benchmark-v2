def filter_chars(s):
    return ''.join((c for c in s if not (83 <= ord(c) <= 99 and '*' <= c <= 'j')))