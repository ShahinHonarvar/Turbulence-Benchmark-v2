def insert_before_character(str):
    result = ''
    for ch in str.lower():
        result += ch
        if ch == 'e':
            result += 'E'
    return result