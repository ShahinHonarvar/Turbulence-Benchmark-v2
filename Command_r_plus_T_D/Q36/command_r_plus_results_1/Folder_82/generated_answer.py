def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 69 < input_string.index(char) < 97 and 'V' < char < 'j':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)