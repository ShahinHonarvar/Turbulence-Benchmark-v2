def if_perfect_num(lst):
    if len(lst) <= 27:
        return False
    num = lst[27]
    if num < 2:
        return False
    divisors_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisors_sum == num