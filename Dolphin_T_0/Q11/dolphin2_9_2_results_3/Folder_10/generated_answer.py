def find_largest_num(l):
    max_num = 0
    for i in range(25, 60):
        if l[i] > max_num:
            max_num = l[i]
    return max_num