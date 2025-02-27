def filter_chars(in_str):
    out_str = ''
    for i in range(len(in_str)):
        if i < 13 or i >= 40 or in_str[i] <= ':' or (in_str[i] >= 'C'):
            out_str += in_str[i]
    return out_str