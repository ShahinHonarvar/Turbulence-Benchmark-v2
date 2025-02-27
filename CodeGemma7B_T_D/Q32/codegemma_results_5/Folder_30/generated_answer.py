def insert_after_character(word):
    result = []
    for letter in word:
        if letter == '4':
            result.append('4')
            result.append('F')
        else:
            result.append(letter)
    return ''.join(result)