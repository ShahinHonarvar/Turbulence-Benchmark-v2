def filter_chars(input_string: str) -> str:
    min_index = 44
    max_index = 48
    filtered_chars = [char for char in input_string if min_index <= ord(char) <= max_index and 'l' > char > '+']
    return ''.join(filtered_chars)