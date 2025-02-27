def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if '1' < char < 'J':
            if 4 <= input_string.index(char) < 8:
                continue
        filtered_string.append(char)
    return ''.join(filtered_string)