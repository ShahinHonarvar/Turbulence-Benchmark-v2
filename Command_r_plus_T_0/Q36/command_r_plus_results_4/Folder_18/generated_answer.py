def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 587 < input_string.index(char) < 648 and char > ',' and (char < 'c'):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)