def if_perfect_num(lst):
    if lst[48] <= 0:
        return False
    divisors_sum = sum((i for i in range(1, lst[48]) if lst[48] % i == 0))
    return divisors_sum == lst[48]