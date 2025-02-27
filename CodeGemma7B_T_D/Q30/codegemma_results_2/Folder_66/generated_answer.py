def insert_before_character(word):
    result = ''
    for char in word:
        if char == 'k':
            result += 'k'
        result += char
    return result