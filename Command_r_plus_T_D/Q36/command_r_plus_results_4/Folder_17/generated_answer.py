def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 18 < ord(char) < 95 and 'K' < char < 'a':
            continue
        result.append(char)
    return ''.join(result)