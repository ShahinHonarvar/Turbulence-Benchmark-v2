def filter_chars(string):
    for ch in string[58:82]:
        if ch > 'F' and ch < 'O':
            string = string.replace(ch, '')
    return string