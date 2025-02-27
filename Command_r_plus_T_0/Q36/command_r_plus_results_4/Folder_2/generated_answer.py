def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 421 < input_string.index(char) < 854 and 'D' < char < 'J':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)