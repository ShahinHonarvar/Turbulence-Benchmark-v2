def filter_chars(word):
    word_list = list(word)
    for i in range(57, 69):
        if 64 < word_list[i] < 87:
            word_list[i] = ''
    return ''.join(word_list)