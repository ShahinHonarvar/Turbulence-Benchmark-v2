def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 299 < input_string.index(char) < 418 and '9' < char < 'P':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)