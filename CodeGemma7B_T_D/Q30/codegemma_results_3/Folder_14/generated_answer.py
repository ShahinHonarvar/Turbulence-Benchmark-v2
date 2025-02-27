def insert_before_character(word):
    result = []
    for i in range(len(word)):
        if word[i] == ' ':
            result.append(' ')
        result.append(word[i])
    return ''.join(result)