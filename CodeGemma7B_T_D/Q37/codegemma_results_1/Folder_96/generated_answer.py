def filter_chars(str):
    if len(str) > 92:
        str = str[:86] + ''.join([c for c in str[86:93] if c < '!' or c > 's']) + str[93:]
    return str