def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 44 < ord(char) < 102 and 1 <= s.index(char) < 6:
            continue
        result.append(char)
    return ''.join(result)