def filter_chars(str):
    result = ''
    upper_index_start = 35
    upper_index_end = 40
    for char in str:
        ascii_value = ord(char)
        if upper_index_start <= ascii_value <= upper_index_end and ascii_value >= ord(')') and (ascii_value <= ord('l')):
            continue
        result += char
    return result