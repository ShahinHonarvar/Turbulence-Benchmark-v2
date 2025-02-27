def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 50 < s.index(char) < 92 and 'A' < char < 'Q':
            continue
        result.append(char)
    return ''.join(result)