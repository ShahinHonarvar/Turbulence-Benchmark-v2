def if_perfect_num(lst):
    if len(lst) <= 15:
        return False
    n = lst[15]
    divisors_sum = sum((i for i in range(1, n) if n % i == 0))
    return divisors_sum == n