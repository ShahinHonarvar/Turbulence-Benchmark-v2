def gcf_three_nums(lst):
    value1 = lst[40]
    value2 = lst[15]
    value3 = lst[99]
    factors = []
    for i in range(1, min(value1, value2, value3) + 1):
        if value1 % i == 0 and value2 % i == 0 and (value3 % i == 0):
            factors.append(i)
    return max(factors)