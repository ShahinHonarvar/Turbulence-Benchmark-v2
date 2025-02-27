def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 52 < s.index(char) < 88 and ord(char) > ord('&') and (ord(char) < ord('c')):
            continue
        result.append(char)
    return ''.join(result)