def filter_chars(input_str: str) -> str:
    for i in range(219, 403):
        if i > ord('*') and i < ord('7'):
            input_str = input_str.replace(chr(i), '')
    return input_str