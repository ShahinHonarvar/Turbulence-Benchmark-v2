def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 31 < ord(char) < 73 and ord(char) > ord('M') and (ord(char) < ord('j')):
            continue
        result.append(char)
    return ''.join(result)