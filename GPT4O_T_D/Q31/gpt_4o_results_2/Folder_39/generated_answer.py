def if_perfect_num(lst):
    if len(lst) <= 59:
        return False
    n = lst[59]
    sum_of_divisors = sum((i for i in range(1, n) if n % i == 0))
    return sum_of_divisors == n