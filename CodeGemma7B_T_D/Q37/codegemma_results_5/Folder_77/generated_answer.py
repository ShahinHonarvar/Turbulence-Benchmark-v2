def filter_chars(str):
    for i in range(384, 412):
        if '/' <= str[i] <= '8':
            str = str.replace(str[i], '')
    return str