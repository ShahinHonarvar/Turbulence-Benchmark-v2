def filter_chars(s):
    result = ''
    chars_to_remove = set()
    for c in s[19:34]:
        if 'S' <= c <= '{':
            chars_to_remove.add(c)
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result