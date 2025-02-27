def filter_chars(input_string: str) -> str:
    filtered_string = []
    for index, char in enumerate(input_string, start=1):
        if 163 < index < 658 and char > '(' and (char < ']'):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)