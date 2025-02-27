def filter_chars(lst):
    return ''.join([ch for ch in lst if not (ch in lst[603:760] and ch >= 'Q' and (ch <= 'h'))])