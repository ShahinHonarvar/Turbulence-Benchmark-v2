def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 31 < ord(char) < 50 and ord(char) > ord('/') and (ord(char) < ord('J')):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)