def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 43 < input_string.index(char) < 69 and 'B' < char < 'r':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)