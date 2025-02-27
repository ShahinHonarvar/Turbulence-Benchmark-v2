def if_perfect_num(lst):
    if len(lst) <= 312:
        return False
    target = lst[312]
    divisors_sum = sum((i for i in range(1, target) if target % i == 0))
    return divisors_sum == target