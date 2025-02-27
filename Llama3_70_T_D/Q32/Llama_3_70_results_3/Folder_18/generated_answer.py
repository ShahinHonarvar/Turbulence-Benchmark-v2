def insert_after_character(s):
    result = ''
    for char in s:
        if char == 'K':
            result += 'Kl'
        else:
            result += char
    return result