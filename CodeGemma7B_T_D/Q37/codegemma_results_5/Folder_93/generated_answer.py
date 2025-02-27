def filter_chars(str):
    filtered_str = ''
    for i, char in enumerate(str):
        if 38 <= i <= 69 and char >= 'H' and (char <= 'e'):
            continue
        filtered_str += char
    return filtered_str