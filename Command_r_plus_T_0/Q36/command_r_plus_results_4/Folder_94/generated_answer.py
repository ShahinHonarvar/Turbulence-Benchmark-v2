def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 15 < s.index(char) < 85 and 'I' < char < 'M':
            continue
        result.append(char)
    return ''.join(result)