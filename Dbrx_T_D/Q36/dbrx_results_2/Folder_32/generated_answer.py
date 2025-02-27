def filter_chars(input_string: str) -> str:
    start_index = 40
    end_index = 63
    filtered_chars = []
    for i, char in enumerate(input_string):
        if start_index <= i < end_index and '7' < char < 'H':
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)