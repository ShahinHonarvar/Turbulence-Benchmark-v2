def if_perfect_num(lst):
    if lst[80] < 0:
        return False
    sum = 1
    for i in range(2, int(lst[80] ** 0.5) + 1):
        if lst[80] % i == 0:
            if i == lst[80] // i:
                sum = sum + i
            else:
                sum = sum + i + lst[80] // i
    return sum == lst[80]