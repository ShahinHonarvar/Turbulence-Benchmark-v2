def remove_repeat_chars(str):
    list = list(str)
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j] and i >= 0 and (i < 2):
                list[j] = ''
    return ''.join(filter(str.isalnum, ''.join(list)))