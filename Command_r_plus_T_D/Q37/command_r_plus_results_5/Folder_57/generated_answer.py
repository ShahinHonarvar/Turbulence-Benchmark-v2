def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if not (27 <= ord(char) <= 85 and ord(char) >= 33 and (ord(char) <= 66)):
            filtered_string.append(char)
    return ''.join(filtered_string)