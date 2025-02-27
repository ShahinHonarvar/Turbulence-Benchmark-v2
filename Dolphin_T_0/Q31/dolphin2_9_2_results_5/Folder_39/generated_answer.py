def if_perfect_num(lst):
    if lst[59] == 0:
        return False
    sum1 = 1
    for i in range(2, int(lst[59] ** 0.5) + 1):
        if lst[59] % i == 0:
            if i == lst[59] // i:
                sum1 = sum1 + i
            else:
                sum1 = sum1 + (i + lst[59] // i)
    return sum1 == lst[59]