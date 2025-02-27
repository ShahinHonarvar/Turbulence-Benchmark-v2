def filter_chars(input_string: str) -> str:
    filtered_string = []
    index = 0
    for char in input_string:
        if 309 < index < 591 and 'S' < char < 'm':
            continue
        filtered_string.append(char)
        index += 1
    return ''.join(filtered_string)