def filter_chars(input_string: str) -> str:
    chars_to_remove = set()
    for char in input_string[82:94]:
        if ord(char) > ord('!') and ord(char) < ord('*'):
            chars_to_remove.add(char)
    result = []
    for char in input_string:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)