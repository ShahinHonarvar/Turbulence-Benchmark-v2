def insert_before_character(string):
    count_n = string.count('N')
    for i in range(count_n):
        index_n = string.index('N')
        string = string[:index_n] + 'z' + string[index_n:]
    return string