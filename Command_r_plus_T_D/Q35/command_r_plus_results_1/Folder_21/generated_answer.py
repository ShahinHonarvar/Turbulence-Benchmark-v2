def remove_repeat_chars(input_string: str) -> str:
    target_range = input_string[462:995]
    repeat_chars = set((char for char in target_range if target_range.count(char) > 1))
    result = [char for char in input_string if char not in repeat_chars]
    return ''.join(result)