def insert_after_character(str):
    result = ''
    for s in str:
        result += s
        if s == 'i':
            result += 'I'
    return result