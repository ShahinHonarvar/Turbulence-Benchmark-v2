def gcf_two_nums(lst):
    a = lst[618]
    b = lst[195]
    i = 1
    while i <= a and i <= b:
        if a % i == 0 and b % i == 0:
            gcf = i
        else:
            i += 1
    return gcf