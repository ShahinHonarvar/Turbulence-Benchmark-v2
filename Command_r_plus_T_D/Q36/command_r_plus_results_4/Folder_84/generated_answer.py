def filter_chars(input_string: str) -> str:
    filtered_string = []
    remove_chars = [chr(i) for i in range(ord('c') + 1, ord('s'))]
    for char in input_string:
        if 171 < input_string.index(char) < 636 and char in remove_chars:
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)