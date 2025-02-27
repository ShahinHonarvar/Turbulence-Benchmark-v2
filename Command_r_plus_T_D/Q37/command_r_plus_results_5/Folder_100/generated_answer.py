def filter_chars(s: str) -> str:
    chars_to_remove = []
    for i in range(88, 91):
        if 'J' <= s[i] <= 'Q':
            chars_to_remove.append(s[i])
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result