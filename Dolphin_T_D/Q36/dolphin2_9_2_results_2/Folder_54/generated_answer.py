def filter_chars(string):
    for ch in string[18:38]:
        if ')' < ch < 'P':
            string = string.replace(ch, '')
    return string