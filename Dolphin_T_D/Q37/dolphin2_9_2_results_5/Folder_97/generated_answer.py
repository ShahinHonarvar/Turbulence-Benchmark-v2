def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if i >= 227 and i <= 235 and (c >= 'D') and (c <= 'u'):
            continue
        result += c
    return result