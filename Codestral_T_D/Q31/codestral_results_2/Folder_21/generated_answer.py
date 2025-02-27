def if_perfect_num(lst):
    num = lst[410]
    sum_div = sum([i for i in range(1, num) if num % i == 0])
    return sum_div == num