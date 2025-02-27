def filter_chars(s):
    result = ''
    chars_to_remove = set()
    for char in s[63:85]:
        if 'E' <= char <= '~':
            chars_to_remove.add(char)
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result