def remove_repeat_chars(a):
    for i in range(45, 67):
        if a[i] in a[45:67]:
            a = a[:i] + a[i + 1:]
    return a