def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 72 < s.index(char) < 93 and ord(char) > ord('<') and (ord(char) < ord('J')):
            continue
        result.append(char)
    return ''.join(result)