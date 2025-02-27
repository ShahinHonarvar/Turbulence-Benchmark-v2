def gcf_three_nums(lst):
    a = lst[9]
    b = lst[6]
    c = lst[2]
    gcf = 1
    for i in range(1, max(a, b, c) + 1):
        if a % i == b % i == c % i == 0:
            gcf = i
    return gcf