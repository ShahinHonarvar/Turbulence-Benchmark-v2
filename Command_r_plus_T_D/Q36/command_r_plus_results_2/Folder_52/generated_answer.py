def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 49 < ord(char) < 56:
            if char > 'I' and char < 'a':
                continue
        result.append(char)
    return ''.join(result)