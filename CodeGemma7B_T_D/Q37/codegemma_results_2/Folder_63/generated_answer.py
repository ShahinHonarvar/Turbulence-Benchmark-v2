def filter_chars(str_in):
    str_out = ''
    for i, letter in enumerate(str_in):
        if i >= 42 and i <= 92 and (letter >= '/') and (letter <= 'a'):
            continue
        str_out += letter
    return str_out