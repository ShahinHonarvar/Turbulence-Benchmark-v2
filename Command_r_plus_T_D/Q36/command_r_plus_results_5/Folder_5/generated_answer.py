def filter_chars(input_string: str) -> str:
    result = list(input_string)
    for char in input_string[55:66]:
        if 'f' < char < '|':
            result = [c for c in result if c != char]
    return ''.join(result)