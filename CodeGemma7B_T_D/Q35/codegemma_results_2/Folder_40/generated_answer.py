def remove_repeat_chars(str):
    l = list(str)
    for i in range(0, 4):
        if l[i] in l[i + 1:4] and l[i] in str:
            str = str.replace(l[i], '')
    return str