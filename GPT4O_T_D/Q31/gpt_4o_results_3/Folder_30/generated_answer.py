def if_perfect_num(lst):
    if len(lst) <= 94:
        return False
    num = lst[94]
    if num < 2:
        return False
    sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_of_divisors == num