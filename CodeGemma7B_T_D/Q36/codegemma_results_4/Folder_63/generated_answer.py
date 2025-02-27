def filter_chars(string):
    return ''.join((c for c in string if not (26 < ord(c) < 80 and c > '<' and (c < '>'))))