def insert_before_character(s: str) -> str:
    new_s = ''
    for char in s:
        if char == 'Q':
            new_s += 'I' + char
        else:
            new_s += char
    return new_s