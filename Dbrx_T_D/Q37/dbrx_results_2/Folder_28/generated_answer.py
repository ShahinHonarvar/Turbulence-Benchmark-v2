def filter_chars(input_string: str) -> str:
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 20 or i > 79 or ord(input_string[i]) < ord('!') or (ord(input_string[i]) > ord('T')):
            filtered_string += input_string[i]
    return filtered_string