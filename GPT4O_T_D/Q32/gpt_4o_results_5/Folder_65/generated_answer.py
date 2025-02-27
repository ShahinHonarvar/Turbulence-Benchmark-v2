def insert_after_character(s: str) -> str:
    result = ''
    for char in s:
        result += char
        if char == '6':
            result += '9'
    return result