def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 1 <= i < 6 and ord(char) > ord(',') and (ord(char) < ord('f')):
            continue
        result.append(char)
    return ''.join(result)