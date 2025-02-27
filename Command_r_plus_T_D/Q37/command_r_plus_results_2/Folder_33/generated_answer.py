def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 722 <= input_string.index(char) <= 832 and 'K' <= char <= 'm':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)