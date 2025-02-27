def filter_chars(input_string: str) -> str:
    filtered_string = input_string[:63] + input_string[63:89].translate({ord(c): None for c in '*' + 'w'}) + input_string[89:]
    return filtered_string