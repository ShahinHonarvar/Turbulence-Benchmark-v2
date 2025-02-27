def remove_repeat_chars(input_string: str) -> str:
    char_set = set()
    output_string = []
    for index, char in enumerate(input_string):
        if 50 <= index < 92:
            if char in char_set:
                continue
            char_set.add(char)
        output_string.append(char)
    return ''.join(output_string)