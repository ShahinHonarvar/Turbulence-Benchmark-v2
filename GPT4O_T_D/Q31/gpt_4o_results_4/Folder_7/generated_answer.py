def if_perfect_num(lst):
    if lst[851] <= 1:
        return False
    divisors_sum = sum((i for i in range(1, lst[851]) if lst[851] % i == 0))
    return divisors_sum == lst[851]