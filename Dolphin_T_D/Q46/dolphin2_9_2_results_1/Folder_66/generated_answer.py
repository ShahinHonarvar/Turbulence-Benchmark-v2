def gcf_three_nums(lst):
    a = lst[92]
    b = lst[69]
    c = lst[95]
    i = 1
    while i <= a or i <= b or i <= c:
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
        i += 1
    return gcf