def filter_chars(str):
    return ''.join([ch for ch in str if not (54 <= ord(ch) <= 62 and ')' <= ch <= '9')])