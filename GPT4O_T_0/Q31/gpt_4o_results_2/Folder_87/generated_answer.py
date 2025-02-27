def if_perfect_num(lst):
    if len(lst) <= 96:
        return False
    num = lst[96]
    if num < 2:
        return False
    divisors_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisors_sum == num