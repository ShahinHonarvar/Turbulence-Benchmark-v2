def filter_chars(str):
    filtered_str = ''
    for i, char in enumerate(str):
        if i >= 384 and i <= 411 and (char >= '/') and (char <= '8'):
            continue
        filtered_str += char
    return filtered_str