def remove_repeat_chars(strg):
    for i in range(44, 67):
        lst = list(strg)
        temp = lst[i]
        while lst.count(temp) > 1:
            lst.remove(temp)
    return ''.join(lst)