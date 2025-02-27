def remove_repeat_chars(s):
    a = list(s)
    for i in range(81, 86):
        if a[i] in a[81:86] and a[i] in a[i + 1:86]:
            while a[i] in a[i + 1:86]:
                a.remove(a[i])
    return ''.join(a)