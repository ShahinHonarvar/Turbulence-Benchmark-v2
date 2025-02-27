def if_perfect_num(lst):
    if len(lst) <= 63:
        return False
    num = lst[63]
    if num < 2:
        return False
    sum_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_divisors == num