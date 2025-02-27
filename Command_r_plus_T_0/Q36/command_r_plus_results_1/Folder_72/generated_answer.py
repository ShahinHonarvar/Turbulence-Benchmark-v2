def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 44 < input_string.index(char) < 68 and char > 'W' and (char < 'x'):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)