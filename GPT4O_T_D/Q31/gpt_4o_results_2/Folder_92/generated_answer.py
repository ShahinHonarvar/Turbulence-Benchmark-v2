def if_perfect_num(lst):
    if not lst:
        return False
    n = lst[0]
    if n < 2:
        return False
    divisors_sum = sum((i for i in range(1, n // 2 + 1) if n % i == 0))
    return divisors_sum == n