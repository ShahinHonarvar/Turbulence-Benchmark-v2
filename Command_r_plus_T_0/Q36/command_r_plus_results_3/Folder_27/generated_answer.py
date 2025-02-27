def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 48 < ord(char) < 75 and char > '6' and (char < '_'):
            continue
        result.append(char)
    return ''.join(result)