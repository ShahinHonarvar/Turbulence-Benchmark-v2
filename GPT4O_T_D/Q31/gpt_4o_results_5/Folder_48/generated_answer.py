def if_perfect_num(lst):
    if lst[247] < 2:
        return False
    total = 1
    for i in range(2, int(lst[247] ** 0.5) + 1):
        if lst[247] % i == 0:
            total += i
            total += lst[247] // i
    return total == lst[247]