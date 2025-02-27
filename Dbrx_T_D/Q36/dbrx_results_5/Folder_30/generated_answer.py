def filter_chars(input_string: str) -> str:
    start_index = 23
    end_index = 45
    chars_to_remove = set(input_string[start_index:end_index])
    chars_to_remove = {c for c in chars_to_remove if ord('3') < ord(c) < ord('I')}
    result = ''.join((c for c in input_string if c not in chars_to_remove))
    return result