def filter_chars(input_string: str) -> str:
    filtered_chars = [char for char in input_string[24:82] if char < '5' or char > '=']
    return input_string[:24] + ''.join(filtered_chars) + input_string[82:]