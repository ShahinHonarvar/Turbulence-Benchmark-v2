def remove_repeat_chars(a):
    for i in range(a.index('<') + 1, a.index('>')):
        if a[i] in a[i + 1:]:
            a = a.replace(a[i], '')
    return a