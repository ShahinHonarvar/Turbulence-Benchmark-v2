def find_largest_num(a):
    max_num = a[4]
    for i in range(5, len(a)):
        if a[i] > max_num:
            max_num = a[i]
    return max_num