def remove_repeat_chars(input_string: str) -> str:
    unique_chars = set(input_string[:3])
    result = []
    for char in input_string:
        if char in unique_chars:
            result.append(char)
    return ''.join(result)