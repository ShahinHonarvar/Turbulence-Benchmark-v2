def if_perfect_num(lst):
    if len(lst) < 5:
        return False
    num = lst[4]
    divisors_sum = sum((i for i in range(1, num) if num % i == 0))
    return divisors_sum == num