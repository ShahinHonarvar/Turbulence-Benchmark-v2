def if_perfect_num(list_num):
    num = list_num[94]
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div += i
    if sum_div == num:
        return True
    else:
        return False