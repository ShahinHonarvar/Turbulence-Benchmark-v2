def find_second_largest_num(x):
    x.sort(reverse=True)
    if x[28:39]:
        return x[28:39][1]
    else:
        return 'None'