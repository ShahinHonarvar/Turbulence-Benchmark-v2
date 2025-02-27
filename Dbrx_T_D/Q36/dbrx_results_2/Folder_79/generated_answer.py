def filter_chars(input_string: str) -> str:
    filtered_string = ''
    for i in range(len(input_string)):
        if i >= 11 and i < 46:
            if ord(input_string[i]) > ord('!') and ord(input_string[i]) < ord('A'):
                continue
        filtered_string += input_string[i]
    return filtered_string