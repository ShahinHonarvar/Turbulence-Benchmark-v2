def filter_chars(input_string: str) -> str:
    start_index = 69
    end_index = 87
    char_range = range(ord('#') + 1, ord('L'))
    chars_to_remove = (c for c in input_string[start_index:end_index] if ord(c) in char_range)
    remove_set = set(chars_to_remove)
    return ''.join((c for c in input_string if c not in remove_set))