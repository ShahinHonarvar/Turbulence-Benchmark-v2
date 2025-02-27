def filter_chars(s):
    result = ''
    to_remove = set()
    for char in s[57:97]:
        if '<' <= char <= 'w':
            to_remove.add(char)
    for char in s:
        if char not in to_remove:
            result += char
    return result