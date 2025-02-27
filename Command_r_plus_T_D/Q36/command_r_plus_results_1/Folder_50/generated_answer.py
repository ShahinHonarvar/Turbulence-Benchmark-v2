def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 61 < s.index(char) < 88 and ord(char) > ord('%') and (ord(char) < ord('q')):
            continue
        result.append(char)
    return ''.join(result)