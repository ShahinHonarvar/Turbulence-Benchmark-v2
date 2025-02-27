def if_perfect_num(lst):
    num = lst[3]
    sum_divisors = sum([i for i in range(1, num) if num % i == 0])
    return num == sum_divisors