def if_perfect_num(lst):
    if lst[4] < 1:
        return False
    sum = 1
    for i in range(2, int(lst[4] ** 0.5) + 1):
        if lst[4] % i == 0:
            if i == lst[4] // i:
                sum = sum + i
            else:
                sum = sum + i + lst[4] // i
    return sum == lst[4]