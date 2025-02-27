def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 86 < input_string.index(char) < 94 and 'E' < char < '~':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)