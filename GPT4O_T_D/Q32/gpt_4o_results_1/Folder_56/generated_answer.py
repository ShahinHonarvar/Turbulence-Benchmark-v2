def insert_after_character(s: str) -> str:
    result = []
    for char in s:
        result.append(char)
        if char == 'I':
            result.append('i')
    return ''.join(result)