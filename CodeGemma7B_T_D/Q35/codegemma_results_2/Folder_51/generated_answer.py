def remove_repeat_chars(a):
    b = a[6:9]
    for char in b:
        k = b.count(char)
        if k > 1:
            for i in range(k - 1):
                b = b.replace(char, '', 1)
    a = a[:6] + b + a[9:]
    return a