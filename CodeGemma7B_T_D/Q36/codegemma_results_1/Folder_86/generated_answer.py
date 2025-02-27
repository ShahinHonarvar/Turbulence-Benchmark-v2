def filter_chars(str):
    for i in range(672, 709):
        if str[i] > 'X' and str[i] < '}':
            str = str.replace(str[i], '')
    return str