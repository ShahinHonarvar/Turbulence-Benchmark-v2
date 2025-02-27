def remove_repeat_chars(input_string: str) -> str:
    target_range = input_string[37:43]
    unique_chars_in_range = set(target_range)
    chars_to_remove = set((char for char in target_range if target_range.count(char) > 1))
    result = ''.join((char for char in input_string if char not in chars_to_remove))
    return result