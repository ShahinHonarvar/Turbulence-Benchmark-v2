def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if i >= 603 and i <= 759 and (c >= 'Q') and (c <= 'h'):
            continue
        result += c
    return result