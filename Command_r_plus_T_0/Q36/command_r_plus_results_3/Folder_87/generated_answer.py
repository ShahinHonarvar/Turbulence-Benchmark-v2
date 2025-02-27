def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 32 < ord(char) < 61 and '3' < char < 'D':
            continue
        result.append(char)
    return ''.join(result)