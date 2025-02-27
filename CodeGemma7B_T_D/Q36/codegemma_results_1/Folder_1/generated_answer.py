def filter_chars(a):
    while 69 < len(a) < 87:
        counter, i = (0, 0)
        while i < len(a):
            if a[i] == a[list(range(69, 87))[counter]]:
                i += 1
                counter += 1
            else:
                a = a[:i] + a[i + 1:]
                i -= 1
    return a