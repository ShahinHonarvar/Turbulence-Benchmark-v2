def return_nth_smallest_ascii(test):
    d = dict(zip(test, map(ord, test)))
    return sorted(d.items(), key=lambda x: x[1])[8][0]