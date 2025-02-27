def filter_chars(input_string: str) -> str:
    filtered_string = []
    for index, char in enumerate(input_string):
        if 50 < index < 92 and 'A' < char < 'Q':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)