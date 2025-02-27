def filter_chars(text):
    result = ''
    for i, c in enumerate(text):
        if i >= 722 and i <= 832 and (c >= 'K') and (c <= 'm'):
            continue
        result += c
    return result