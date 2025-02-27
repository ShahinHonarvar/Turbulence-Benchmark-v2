def filter_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(23, 90):
        if 'w' <= s[i] <= '{':
            chars_to_remove.add(s[i])
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result