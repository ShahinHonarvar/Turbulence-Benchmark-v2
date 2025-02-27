def filter_chars(input_string: str) -> str:
    result = list(input_string)
    for char_index in range(421, 854):
        char = input_string[char_index]
        if 'D' < char < 'J':
            result = [c for c in result if c != char]
    return ''.join(result)