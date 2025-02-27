def insert_after_character(word):
    result = ''
    for char in word:
        result += char
        if char == 'e':
            result += 'W'
    return result