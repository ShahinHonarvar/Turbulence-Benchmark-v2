def gcf_two_nums(lst):
    a = lst[51]
    b = lst[31]
    for i in range(max(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i