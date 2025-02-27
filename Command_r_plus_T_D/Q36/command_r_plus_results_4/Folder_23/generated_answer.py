def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 21 < input_string.index(char) < 25 and '5' < char < '}':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)