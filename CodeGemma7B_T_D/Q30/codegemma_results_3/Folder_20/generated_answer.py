def insert_before_character(str):
    word = str.split('C')
    str = word[0] + 'H'
    for i in range(len(word) - 1):
        str += word[i + 1]
    return str