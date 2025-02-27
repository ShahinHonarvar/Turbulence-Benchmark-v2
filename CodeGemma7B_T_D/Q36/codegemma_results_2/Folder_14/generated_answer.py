def filter_chars(a):
    for i in range(len(a)):
        if a[i] <= 'Z' and a[i] >= 'c' and (i > 41) and (i < 56):
            a = a[:i] + a[i + 1:]
            i -= 1
    return a