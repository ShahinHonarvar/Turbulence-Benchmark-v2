def remove_repeat_chars(a):
    for i in a[56:90]:
        if i in a[56:90]:
            a = a.replace(i, '')
    return a