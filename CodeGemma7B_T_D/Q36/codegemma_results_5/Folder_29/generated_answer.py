def filter_chars(a):
    b = ''
    for i in range(len(a)):
        if i >= 46 and i <= 68:
            if a[i] > 'H' and a[i] < 's':
                continue
        b += a[i]
    return b