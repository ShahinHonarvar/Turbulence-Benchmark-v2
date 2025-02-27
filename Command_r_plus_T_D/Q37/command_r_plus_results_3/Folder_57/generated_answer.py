def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if not (27 <= ord(char) <= 85 and ord(char) >= 33 and (ord(char) <= 66)):
            result.append(char)
    return ''.join(result)