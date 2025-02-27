def if_perfect_num(lst):
    if lst[95] > 0:
        num = lst[95]
        sum_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_divisors == num
    return False