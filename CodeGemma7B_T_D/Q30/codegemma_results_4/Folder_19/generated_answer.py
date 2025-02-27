def insert_before_character(word):
    result = ''
    for char in word:
        if char == '5':
            result += 'h' + char
        else:
            result += char
    return result