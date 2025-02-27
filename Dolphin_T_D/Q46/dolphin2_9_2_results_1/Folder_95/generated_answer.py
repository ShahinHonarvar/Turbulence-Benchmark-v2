def gcf_three_nums(lst):
    a = lst[87]
    b = lst[20]
    c = lst[36]
    i = 1
    gcf = 1
    while i <= a and i <= b and (i <= c):
        if a % i == b % i == c % i == 0:
            gcf = i
        i += 1
    return gcf