def filter_chars(input_str):
    filtered_str = ''
    for i, char in enumerate(input_str):
        if 259 <= i <= 502 and ',' <= char <= '3':
            continue
        filtered_str += char
    return filtered_str