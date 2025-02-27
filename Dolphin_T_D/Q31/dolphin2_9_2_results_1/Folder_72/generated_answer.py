def if_perfect_num(lst):
    if not lst or not isinstance(lst[16], int) or lst[16] <= 0:
        return False
    sum_factors = 0
    for i in range(1, lst[16] // 2 + 1):
        if lst[16] % i == 0:
            sum_factors += i
    return sum_factors == lst[16]