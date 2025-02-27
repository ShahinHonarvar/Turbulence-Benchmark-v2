def filter_chars(str):
    filtered_str = []
    for i in range(24, 37):
        if str[i] > 'A' and str[i] < 'h':
            filtered_str.append(str[i])
    return ''.join(filtered_str)