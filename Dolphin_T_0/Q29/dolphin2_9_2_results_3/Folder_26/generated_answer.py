def gcf_two_nums(lst):
    a = lst[49]
    b = lst[31]
    if a < b:
        smaller = a
    else:
        smaller = b
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            gcf = i
    return gcf