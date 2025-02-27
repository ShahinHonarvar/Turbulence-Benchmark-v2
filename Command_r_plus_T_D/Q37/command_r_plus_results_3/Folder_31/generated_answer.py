def filter_chars(s: str) -> str:
    chars_to_remove = []
    for i in range(57, 97):
        if chr(i) >= '<' and chr(i) <= 'w':
            chars_to_remove.append(chr(i))
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result