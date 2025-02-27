def if_perfect_num(lst):
    if len(lst) <= 849:
        return False
    number = lst[849]
    divisors_sum = sum((i for i in range(1, number) if number % i == 0))
    return divisors_sum == number