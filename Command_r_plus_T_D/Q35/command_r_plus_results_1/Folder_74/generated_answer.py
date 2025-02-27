def remove_repeat_chars(input_string: str) -> str:
    repeat_chars = {}
    for char in input_string[69:97]:
        if char in repeat_chars:
            repeat_chars[char] += 1
        else:
            repeat_chars[char] = 1
    result = []
    for char in input_string:
        if char in repeat_chars and repeat_chars[char] > 1:
            continue
        result.append(char)
    return ''.join(result)