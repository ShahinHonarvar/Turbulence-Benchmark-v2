def filter_chars(string):
    for ch in string[24:37]:
        if 'A' < ch < 'h':
            string = string.replace(ch, '')
    return string