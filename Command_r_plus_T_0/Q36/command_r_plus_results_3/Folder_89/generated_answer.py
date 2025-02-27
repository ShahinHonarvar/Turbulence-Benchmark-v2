def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 57 <= input_string.index(char) < 69 and ord(char) > ord('(') and (ord(char) < ord('W')):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)