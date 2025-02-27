def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 31 < ord(char) < 70 and ord(char) > ord('B') and (ord(char) < ord('v')):
            continue
        result.append(char)
    return ''.join(result)