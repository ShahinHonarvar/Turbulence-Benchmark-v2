def filter_chars(str):
    s = str[0:14] + ''.join([ch for ch in str[14:75] if not '9' < ch < 'K'], str[75:])
    return s