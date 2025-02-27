def insert_before_character(text):
    text_list = list(text)
    for i in range(len(text_list)):
        if text_list[i] == 'o':
            text_list[i] = 'o' + text_list[i]
    return ''.join(text_list)