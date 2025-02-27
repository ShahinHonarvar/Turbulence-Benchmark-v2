def filter_chars(input_string: str) -> str:
    filtered_string = []
    for index, char in enumerate(input_string):
        if 309 <= index < 591 and 'S' < char < 'm':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)