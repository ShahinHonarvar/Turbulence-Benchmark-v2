def if_perfect_num(lst):
    if len(lst) <= 53:
        return False
    num = lst[53]
    if num < 2:
        return False
    divisors_sum = sum((i for i in range(1, num // 2 + 1) if num % i == 0))
    return divisors_sum == num