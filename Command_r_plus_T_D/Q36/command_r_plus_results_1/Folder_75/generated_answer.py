def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 46 < ord(char) < 74 and ord(char) > ord('&') and (ord(char) < ord('M')):
            continue
        result.append(char)
    return ''.join(result)