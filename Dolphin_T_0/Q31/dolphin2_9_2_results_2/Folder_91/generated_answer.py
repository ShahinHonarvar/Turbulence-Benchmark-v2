def if_perfect_num(lst):
    if len(lst) < 7:
        return False
    num = lst[6]
    sum_div = 1
    for i in range(2, num):
        if num % i == 0:
            sum_div += i
    return sum_div == num