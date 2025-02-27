def filter_chars(input_string: str) -> str:
    filtered_string = []
    for i, char in enumerate(input_string):
        if 669 < i < 888 and 'B' < char < 'Y':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)