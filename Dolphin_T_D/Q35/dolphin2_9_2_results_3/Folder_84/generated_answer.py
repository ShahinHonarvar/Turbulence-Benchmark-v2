def remove_repeat_chars(string):
    char_dict = {}
    for i in range(32, 44):
        if string[i] in char_dict:
            char_dict[string[i]] += 1
        else:
            char_dict[string[i]] = 1
    for char, count in char_dict.items():
        if count > 1:
            string = string.replace(char, '')
    return string