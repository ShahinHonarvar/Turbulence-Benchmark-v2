def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 46 < ord(char) < 91 and ord('D') < ord(char) < ord('H'):
            continue
        result.append(char)
    return ''.join(result)