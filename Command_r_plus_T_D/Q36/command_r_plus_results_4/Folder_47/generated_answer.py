def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 45 < ord(char) < 57 and 'F' < char < 'n':
            continue
        result.append(char)
    return ''.join(result)