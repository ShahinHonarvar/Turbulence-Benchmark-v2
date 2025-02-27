def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 39 < s.index(char) < 87 and ord(char) > ord('!') and (ord(char) < ord('}')):
            continue
        result.append(char)
    return ''.join(result)