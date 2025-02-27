def if_perfect_num(lst):
    if len(lst) <= 849:
        return False
    num = lst[849]
    if num < 2:
        return False
    sum_div = sum((i for i in range(1, num) if num % i == 0))
    return sum_div == num