def remove_repeat_chars(input_string: str) -> str:
    repeat_chars = set(input_string[68:99])
    repeat_chars = set([char for char in repeat_chars if input_string.count(char) > 1])
    result = []
    for char in input_string:
        if char in repeat_chars:
            continue
        result.append(char)
    return ''.join(result)