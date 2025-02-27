def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 55 < input_string.index(char) < 80 and 'S' < char < 's':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)