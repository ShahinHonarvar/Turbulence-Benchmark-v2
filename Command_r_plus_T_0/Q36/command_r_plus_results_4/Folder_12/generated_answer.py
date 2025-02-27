def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 32 < ord(char) < 84 and ord('m') < ord(char) < ord('w'):
            continue
        result.append(char)
    return ''.join(result)