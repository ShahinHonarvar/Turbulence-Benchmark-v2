def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 39 < s.index(char) < 87 and '!' < char < '}':
            continue
        result.append(char)
    return ''.join(result)