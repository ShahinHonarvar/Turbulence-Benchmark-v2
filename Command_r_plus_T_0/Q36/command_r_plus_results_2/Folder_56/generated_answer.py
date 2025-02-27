def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 31 < ord(char) < 50 and ord(char) > ord('/') and (ord(char) < ord('J')):
            continue
        result.append(char)
    return ''.join(result)