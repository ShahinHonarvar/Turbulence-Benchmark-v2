def filter_chars(input_str):
    for i in range(18, 95):
        ch = input_str[i]
        if ch > 'K' and ch < 'a':
            input_str = input_str.replace(ch, '')
    return input_str