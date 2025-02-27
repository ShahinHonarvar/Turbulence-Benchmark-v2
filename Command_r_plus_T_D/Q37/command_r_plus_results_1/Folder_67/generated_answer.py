def filter_chars(s: str) -> str:
    chars_to_remove = []
    for char in s[19:23]:
        if ']' <= char <= 't':
            chars_to_remove.append(char)
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result