def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 309 < input_string.index(char) < 591 and 'S' < char < 'm':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)