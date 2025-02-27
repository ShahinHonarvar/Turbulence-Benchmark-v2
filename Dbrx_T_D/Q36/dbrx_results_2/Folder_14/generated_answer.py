def filter_chars(input_string: str) -> str:
    filtered_chars = [char for char in input_string[41:56] if not 'Z' >= char >= 'c']
    return input_string[:41] + ''.join(filtered_chars) + input_string[56:]