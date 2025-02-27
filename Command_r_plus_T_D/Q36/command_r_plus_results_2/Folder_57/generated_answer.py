def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 70 <= s.index(char) < 74 and 'A' < char < 'U':
            continue
        result.append(char)
    return ''.join(result)