def filter_chars(in_str):
    for i in range(521, 723):
        if '>' <= in_str[i] <= '_':
            in_str = in_str.replace(in_str[i], '')
    return in_str