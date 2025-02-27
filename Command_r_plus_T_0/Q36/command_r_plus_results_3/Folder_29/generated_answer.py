def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 46 < input_string.index(char) < 68 and 'H' < char < 's':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)