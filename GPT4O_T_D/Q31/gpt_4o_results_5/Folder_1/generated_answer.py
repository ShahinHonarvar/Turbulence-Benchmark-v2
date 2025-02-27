def if_perfect_num(lst):
    if len(lst) > 85:
        num = lst[85]
        divisors_sum = sum((i for i in range(1, num) if num % i == 0))
        return divisors_sum == num
    return False