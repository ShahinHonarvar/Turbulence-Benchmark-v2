def filter_chars(str):
    str = str[:114] + ''.join([c for c in str[114:639] if c < '!' or c > 'x']) + str[639:]
    return str