def gcf_two_nums(lst):
    a = lst[17]
    b = lst[20]
    if a < b:
        small = a
    else:
        small = b
    for i in range(1, small + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd