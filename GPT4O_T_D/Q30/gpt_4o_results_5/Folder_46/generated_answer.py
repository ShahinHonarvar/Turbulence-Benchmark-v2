def insert_before_character(s: str) -> str:
    result = []
    for char in s:
        if char == '6':
            result.append('W')
        result.append(char)
    return ''.join(result)