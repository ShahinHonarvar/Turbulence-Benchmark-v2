def if_perfect_num(lst):
    if len(lst) < 2:
        return False
    num = lst[1]
    if num < 2:
        return False
    divisor_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisor_sum == num