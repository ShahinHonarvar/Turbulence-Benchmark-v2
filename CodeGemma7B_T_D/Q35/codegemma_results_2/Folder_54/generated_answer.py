def remove_repeat_chars(string):
    char_dict = {}
    for i in range(35, 64):
        if string[i] in char_dict:
            while string[i] in string[i + 1:]:
                string = string.replace(string[i], '', 1)
            char_dict[string[i]] = i
        else:
            char_dict[string[i]] = i
    return string