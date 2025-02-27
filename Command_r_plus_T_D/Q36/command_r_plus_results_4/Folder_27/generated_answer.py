def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 48 < ord(char) < 75 and char > '6' and (char < '_'):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)