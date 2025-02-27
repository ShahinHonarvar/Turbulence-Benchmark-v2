def insert_after_character(word):
    temp = list(word)
    for i in range(len(temp)):
        if temp[i] == 'U':
            temp.insert(i + 1, 'u')
    return ''.join(temp)