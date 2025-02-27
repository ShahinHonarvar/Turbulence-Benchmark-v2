def remove_repeat_chars(string):
    str_list = list(string)
    for i in range(22, 24):
        if str_list.count(str_list[i]) > 1:
            str_list = [char for char in str_list if char != str_list[i]]
    return ''.join(str_list)