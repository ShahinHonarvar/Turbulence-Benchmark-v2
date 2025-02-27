def if_perfect_num(lst):
    if len(lst) <= 83:
        return False
    num = lst[83]
    if num < 2:
        return False
    divisors_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisors_sum == num