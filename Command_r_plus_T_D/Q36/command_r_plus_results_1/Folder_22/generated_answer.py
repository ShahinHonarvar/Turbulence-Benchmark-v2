def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 55 < s.index(char) < 84 and ord(char) > ord(';') and (ord(char) < ord('z')):
            continue
        result.append(char)
    return ''.join(result)