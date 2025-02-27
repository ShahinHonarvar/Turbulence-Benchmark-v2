def filter_chars(input_string: str) -> str:
    start_index = 54
    end_index = 92
    chars_to_remove = set(input_string[start_index:end_index])
    chars_to_remove = {c for c in chars_to_remove if 'J' < c < 'X'}
    result = ''.join((c for c in input_string if c not in chars_to_remove))
    return result