def filter_chars(input_string: str) -> str:
    filtered_string = []
    for index, char in enumerate(input_string):
        if 344 < index < 874 and 'f' < char < '~':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)