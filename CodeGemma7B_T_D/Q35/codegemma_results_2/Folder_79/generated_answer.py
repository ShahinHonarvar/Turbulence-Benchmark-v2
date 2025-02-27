def remove_repeat_chars(a):
    for i in range(1, 8):
        for j in range(i + 1, 8):
            if a[i] == a[j]:
                while a[j] == a[i]:
                    a = a[:j] + a[j + 1:]
    return a