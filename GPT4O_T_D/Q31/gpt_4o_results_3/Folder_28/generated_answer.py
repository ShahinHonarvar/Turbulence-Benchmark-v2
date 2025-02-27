def if_perfect_num(lst):
    if len(lst) > 37:
        num = lst[37]
        if num > 0:
            divisors_sum = sum((i for i in range(1, num) if num % i == 0))
            return divisors_sum == num
    return False