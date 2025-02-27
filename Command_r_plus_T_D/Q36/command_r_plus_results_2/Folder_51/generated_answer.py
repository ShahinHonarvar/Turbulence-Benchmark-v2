def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 58 < s.index(char) < 81 and '5' < char < '>':
            continue
        result.append(char)
    return ''.join(result)