def remove_repeat_chars(str):
    l = list(str)
    for i in range(0, 10):
        a = l[i]
        if a * 2 in l:
            while a * 2 in l:
                l.remove(a)
    return ''.join(l)