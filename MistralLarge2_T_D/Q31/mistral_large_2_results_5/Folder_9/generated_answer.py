def is_perfect_number(n):
    sum_of_divisors = sum([i for i in range(1, n) if n % i == 0])
    return sum_of_divisors == n

def if_perfect_num(lst):
    return is_perfect_number(lst[24]) if len(lst) > 24 else False