def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 10 <= s.index(char) < 79 and '?' < char < 'm':
            continue
        result.append(char)
    return ''.join(result)