def filter_chars(a):
    for i in range(31, 50):
        if ord(a[i]) > ord('/') and ord(a[i]) < ord('J'):
            a = a.replace(a[i], '')
    return a