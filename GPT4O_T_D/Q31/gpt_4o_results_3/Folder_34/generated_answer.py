def if_perfect_num(lst):
    if len(lst) > 97:
        num = lst[97]
        if num > 1:
            sum_divisors = sum((i for i in range(1, num) if num % i == 0))
            return sum_divisors == num
    return False