def filter_chars(input_string: str) -> str:
    result = list(input_string)
    for char in input_string[46:68]:
        if 'H' < char < 's':
            result = [c for c in result if c != char]
    return ''.join(result)