def remove_repeat_chars(string):
    char_list = []
    new_string = ''
    for i in range(len(string)):
        if i < 30 or i > 200:
            new_string += string[i]
        elif string[i] not in char_list:
            char_list.append(string[i])
            new_string += string[i]
    return new_string