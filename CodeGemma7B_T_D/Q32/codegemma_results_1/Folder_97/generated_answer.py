def insert_after_character(text):
    result = text
    index = 0
    while index < len(result):
        if result[index] == 'o':
            result = result[:index + 1] + 'h' + result[index + 1:]
        index += 1
    return result