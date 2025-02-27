def if_perfect_num(lst):
    total = 0
    for i in range(1, lst[126]):
        if lst[126] % i == 0:
            total += i
    return total == lst[126]