def remove_repeat_chars(a):
    b = []
    for i in range(len(a)):
        if i >= 35 and i < 64 and (a[i] in b):
            continue
        b.append(a[i])
    c = ''.join(b)
    return c