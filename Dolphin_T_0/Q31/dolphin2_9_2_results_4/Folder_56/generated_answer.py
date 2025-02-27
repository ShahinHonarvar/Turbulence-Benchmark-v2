def if_perfect_num(lst):
    num = lst[60]
    sum_div = sum((1 for i in range(1, num) if num % i == 0))
    return sum_div == num