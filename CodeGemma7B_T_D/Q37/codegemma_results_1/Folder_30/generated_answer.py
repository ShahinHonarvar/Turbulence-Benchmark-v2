def filter_chars(s):
    return ''.join([ch for ch in s if not (41 <= ord(ch) <= 64 and 'K' <= ch <= ']')])