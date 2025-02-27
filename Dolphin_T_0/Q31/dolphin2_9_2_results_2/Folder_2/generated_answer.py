def if_perfect_num(lst):
    if len(lst) < 703:
        return False
    num = lst[702]
    sum_divisors = 1 + sum([i for i in range(2, int(num ** 0.5) + 1) if num % i == 0] + [num // i for i in range(2, int(num ** 0.5) + 1) if i * i != num and num % i == 0])
    return sum_divisors == num