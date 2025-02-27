def filter_chars(s: str) -> str:
    chars_to_remove = []
    for i in range(502, 946):
        if 'W' < s[i] < 'y':
            chars_to_remove.append(s[i])
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result