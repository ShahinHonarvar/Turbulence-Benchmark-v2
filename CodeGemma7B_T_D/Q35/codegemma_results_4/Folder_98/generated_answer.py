def remove_repeat_chars(input_str):
    seen_chars = set()
    result = []
    for char in input_str:
        if char in seen_chars or index(char) > 7:
            continue
        seen_chars.add(char)
        result.append(char)
    return ''.join(result)