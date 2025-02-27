def filter_chars(x):
    y = []
    for i in range(669, 888):
        if x[i] > 'B' and x[i] < 'Y':
            continue
        else:
            y.append(x[i])
    return ''.join(y)