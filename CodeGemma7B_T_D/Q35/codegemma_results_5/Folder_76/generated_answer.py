def remove_repeat_chars(input_string):
    seen_chars = set()
    result = []
    for char in input_string:
        if char in seen_chars:
            continue
        seen_chars.add(char)
        if 330 <= input_string.index(char) <= 543:
            if char in result:
                result.remove(char)
        else:
            result.append(char)
    return ''.join(result)