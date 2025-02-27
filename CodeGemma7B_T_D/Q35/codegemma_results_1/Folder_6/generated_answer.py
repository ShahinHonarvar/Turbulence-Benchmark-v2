def remove_repeat_chars(a):
    for i in range(20, 93):
        while a.find(a[i], i + 1) != -1:
            a = a[:a.find(a[i], i + 1)] + a[a.find(a[i], i + 1) + 1:]
    return a