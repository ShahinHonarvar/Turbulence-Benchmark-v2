def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 54 < input_string.index(char) < 92 and 'J' < char < 'X':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)