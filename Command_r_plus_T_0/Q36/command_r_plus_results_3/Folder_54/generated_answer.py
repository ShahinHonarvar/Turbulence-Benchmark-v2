def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 18 < input_string.index(char) < 38 and ')' < char < 'P':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)