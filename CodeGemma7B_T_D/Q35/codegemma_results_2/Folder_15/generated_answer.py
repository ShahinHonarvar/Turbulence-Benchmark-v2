def remove_repeat_chars(a):
    b = []
    for i in range(len(a)):
        if i < 4 and a[i] not in b:
            b.append(a[i])
    return ''.join(b)