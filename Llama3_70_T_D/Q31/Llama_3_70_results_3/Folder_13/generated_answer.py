def if_perfect_num(lst):
    if len(lst) > 126:
        num = lst[126]
        sum_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_divisors == num
    return False