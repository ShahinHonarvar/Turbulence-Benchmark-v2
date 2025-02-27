def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 71 <= ord(char) <= 96 and ord(char) >= ord('_') and (ord(char) <= ord('o')):
            continue
        result.append(char)
    return ''.join(result)