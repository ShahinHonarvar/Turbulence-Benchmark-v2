def filter_chars(str_in):
    str_out = ''
    for i in range(len(str_in)):
        if i >= 83 and i <= 99 and (str_in[i] >= '*') and (str_in[i] <= 'j'):
            continue
        str_out += str_in[i]
    return str_out