def is_perfect_number(num):
    if num < 2:
        return False
    sum_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_divisors == num

def if_perfect_num(lst):
    if len(lst) > 34:
        return is_perfect_number(lst[34])
    return False