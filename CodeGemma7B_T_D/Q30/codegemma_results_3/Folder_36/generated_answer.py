def insert_before_character(word):
    index_list = []
    for i in range(len(word)):
        if word[i] == 'A':
            index_list.append(i)
    for i in range(len(index_list)):
        word_new = word[:index_list[i]] + 'H' + word[index_list[i]:]
    return word_new