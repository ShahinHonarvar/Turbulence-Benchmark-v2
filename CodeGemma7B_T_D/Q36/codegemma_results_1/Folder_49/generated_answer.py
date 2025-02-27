def filter_chars(s):
    filtered_string = ''
    for i in range(46, 91):
        if s[i] <= 'H' and s[i] > 'D':
            continue
        filtered_string += s[i]
    return filtered_string