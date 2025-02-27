def filter_chars(s: str) -> str:
    to_remove = []
    for i in range(31, 39):
        if ';' <= chr(i) <= 'g':
            to_remove.append(chr(i))
    result = ''
    for char in s:
        if char not in to_remove:
            result += char
    return result