def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 27 <= ord(char) <= 29 and ';' <= char <= 'b':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)