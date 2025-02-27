def filter_chars(input_str):
    new_str = ''
    for char in input_str:
        if ord(char) >= ord('X') and ord(char) <= ord('p') and (input_str.index(char) >= 51) and (input_str.index(char) <= 96):
            continue
        else:
            new_str += char
    return new_str