def filter_chars(text):
    return ''.join([ch for ch in text if 64 >= ord(ch) <= 126 and (not (1 <= ord(ch) <= 5 and '$' <= ch <= ';'))])