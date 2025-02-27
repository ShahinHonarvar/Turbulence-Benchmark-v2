def remove_repeat_chars(input_string: str) -> str:
    target_range = input_string[355:988]
    unique_chars = set(target_range)
    result = []
    for char in input_string:
        if char in unique_chars:
            continue
        result.append(char)
    return ''.join(result)