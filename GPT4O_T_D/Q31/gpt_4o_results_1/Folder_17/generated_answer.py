def if_perfect_num(lst):
    if len(lst) <= 632:
        return False
    num = lst[632]
    sum_factors = sum((i for i in range(1, num) if num % i == 0))
    return sum_factors == num