def filter_chars(str):
    filtered_str = ''
    for i, char in enumerate(str):
        if i <= 5 and (char >= '$' and char <= ';'):
            continue
        filtered_str += char
    return filtered_str