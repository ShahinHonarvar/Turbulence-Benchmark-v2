def gcf_two_nums(lst):
    a = lst[66]
    b = lst[90]
    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            return i