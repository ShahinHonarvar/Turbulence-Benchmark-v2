def filter_chars(s):
    return ''.join([a for a in s if not (a >= chr(155) and a <= chr(403) and (a >= '(') and (a <= '['))])