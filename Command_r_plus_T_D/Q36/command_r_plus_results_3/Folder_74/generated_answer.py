def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 33 < ord(char) < 36 and char > '>' and (char < 'A'):
            continue
        result.append(char)
    return ''.join(result)