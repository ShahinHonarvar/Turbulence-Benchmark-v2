def filter_chars(input_string: str) -> str:
    filtered_string = []
    for index, char in enumerate(input_string):
        if 42 <= index < 68 and 't' < char < 'x':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)