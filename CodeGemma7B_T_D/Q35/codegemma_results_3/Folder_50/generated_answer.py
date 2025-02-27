def remove_repeat_chars(str):
    new_str = ''
    for i in range(13, 76):
        if str[i] not in new_str:
            new_str += str[i]
    return new_str