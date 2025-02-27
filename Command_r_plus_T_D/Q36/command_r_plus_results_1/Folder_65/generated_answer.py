def filter_chars(input_string: str) -> str:
    filtered_string = ''
    for char in input_string:
        if 58 < ord(char) < 82 and 'F' < char < 'O':
            continue
        filtered_string += char
    return filtered_string