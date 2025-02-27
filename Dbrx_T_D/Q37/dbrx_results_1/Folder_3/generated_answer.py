def filter_chars(input_string: str) -> str:
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 37 or i > 56 or ord(input_string[i]) < ord('6') or (ord(input_string[i]) > ord('_')):
            filtered_string += input_string[i]
    return filtered_string