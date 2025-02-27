def filter_chars(x):
    for i in range(587, 648):
        if x[i] > ',' and x[i] < 'c':
            x = x.replace(x[i], '')
    return x