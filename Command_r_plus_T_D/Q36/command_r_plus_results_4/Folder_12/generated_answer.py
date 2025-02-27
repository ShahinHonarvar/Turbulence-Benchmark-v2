def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 32 < ord(char) < 84 and 'm' < char < 'w':
            continue
        result.append(char)
    return ''.join(result)