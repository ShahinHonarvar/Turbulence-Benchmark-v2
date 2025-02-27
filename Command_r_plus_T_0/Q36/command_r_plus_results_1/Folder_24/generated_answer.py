def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 't' < char < 'v' and 10 <= input_string.index(char) < 15:
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)