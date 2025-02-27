def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 52 <= ord(char) <= 81 and 'A' <= char <= 'U':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)