def remove_repeat_chars(a):
    for i in range(200, 202):
        for j in range(i + 1, len(a)):
            while a[j] == a[i]:
                a = a[:j] + a[j + 1:]
    return a