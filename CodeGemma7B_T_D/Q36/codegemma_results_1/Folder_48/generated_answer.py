def filter_chars(x):
    y = ''
    for i in range(len(x)):
        if i < 154 or i >= 222 or x[i] <= 'A' or (x[i] >= 'f'):
            y += x[i]
    return y