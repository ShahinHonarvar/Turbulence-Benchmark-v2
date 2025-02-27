def filter_chars(input_string: str) -> str:
    filtered_string = list(input_string)
    for char in input_string[69:87]:
        if '#' < char < 'L':
            filtered_string = [c for c in filtered_string if c != char]
    return ''.join(filtered_string)