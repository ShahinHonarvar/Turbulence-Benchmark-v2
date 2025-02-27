def filter_chars(str):
    filtered_str = ''
    for char in str:
        if str.index(char) >= 38 and str.index(char) <= 54 and (char >= ':') and (char <= 'r'):
            continue
        else:
            filtered_str += char
    return filtered_str