def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 41 < s.index(char) < 56 and ord(char) > ord('Z') and (ord(char) < ord('c')):
            continue
        result.append(char)
    return ''.join(result)