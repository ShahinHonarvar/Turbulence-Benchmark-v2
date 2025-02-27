def remove_repeat_chars(str_to_mod):
    new_list = []
    for i in str_to_mod:
        if len(new_list) < 37 or new_list[len(new_list) - 1] != i:
            new_list.append(i)
    return ''.join(new_list)