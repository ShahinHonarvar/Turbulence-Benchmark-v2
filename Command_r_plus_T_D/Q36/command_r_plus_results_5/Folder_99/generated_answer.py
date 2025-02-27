def filter_chars(s: str) -> str:
    result = []
    remove_chars = set()
    for char in s[476:948]:
        if 'b' < char < 'd':
            remove_chars.add(char)
    for char in s:
        if char not in remove_chars:
            result.append(char)
    return ''.join(result)