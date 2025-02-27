def filter_chars(s: str) -> str:
    chars_to_remove = []
    for i in range(72, 95):
        char = chr(i)
        if '.' <= char <= 'b':
            chars_to_remove.append(char)
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result