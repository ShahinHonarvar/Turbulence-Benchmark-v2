def insert_before_character(s: str) -> str:
    result = []
    for c in s:
        if c == 'U':
            result.append('q')
        result.append(c)
    return ''.join(result)