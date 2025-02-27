def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 502 < input_string.index(char) < 946 and 'W' < char < 'y':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)