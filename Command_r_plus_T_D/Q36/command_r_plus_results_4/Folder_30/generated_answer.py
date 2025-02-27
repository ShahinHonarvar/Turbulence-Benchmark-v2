def filter_chars(input_string: str) -> str:
    filtered_string = []
    for index, char in enumerate(input_string):
        if 23 <= index < 45 and '3' < char < 'I':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)