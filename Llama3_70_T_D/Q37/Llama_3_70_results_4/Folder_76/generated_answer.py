def filter_chars(s):
    chars_to_remove = set()
    for char in s[379:899]:
        if 'M' <= char <= 'v':
            chars_to_remove.add(char)
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result