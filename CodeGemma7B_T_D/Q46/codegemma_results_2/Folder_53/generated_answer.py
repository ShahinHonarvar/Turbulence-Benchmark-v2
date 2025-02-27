def gcf_three_nums(x):
    a, b, c = (x[66], x[56], x[92])
    return gcf(a, gcf(b, c))