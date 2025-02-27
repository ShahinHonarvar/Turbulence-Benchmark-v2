def filter_chars(str):
    return ''.join((ch for ch in str if not (20 <= ord(ch) <= 32 and 'f' <= ch <= 'o')))