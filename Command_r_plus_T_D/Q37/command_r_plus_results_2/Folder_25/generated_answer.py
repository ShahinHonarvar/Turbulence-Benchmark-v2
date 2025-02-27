def filter_chars(input_string: str) -> str:
    filtered_string = ''
    for char in input_string:
        if 31 <= ord(char) <= 38 and ';' <= char <= 'g':
            continue
        filtered_string += char
    return filtered_string