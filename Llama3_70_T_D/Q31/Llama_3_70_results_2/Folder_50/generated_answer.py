def if_perfect_num(num_list):
    if len(num_list) < 41:
        return False
    n = num_list[40]
    sum_divisors = sum((i for i in range(1, n) if n % i == 0))
    return sum_divisors == n