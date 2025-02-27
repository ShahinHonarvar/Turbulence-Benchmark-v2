def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 15 < input_string.index(char) < 85 and 'I' < char < 'M':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)