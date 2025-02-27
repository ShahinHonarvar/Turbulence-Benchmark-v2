def filter_chars(s):
    return ''.join([ch for ch in s if not (219 <= ord(ch) <= 403 and ch > '*' and (ch < '7'))])