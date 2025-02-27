def filter_chars(s):
    new_str = ''
    for idx, char in enumerate(s):
        if idx >= 36 and idx <= 79 and (char >= 'a') and (char <= 'i'):
            continue
        else:
            new_str += char
    return new_str