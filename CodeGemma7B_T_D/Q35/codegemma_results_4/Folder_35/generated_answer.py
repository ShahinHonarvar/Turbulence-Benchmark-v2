def remove_repeat_chars(str):
    str_list = list(str)
    for char in str_list[77:84]:
        if str_list.count(char) > 1:
            while str_list.count(char) > 1:
                str_list.remove(char)
    return ''.join(str_list)