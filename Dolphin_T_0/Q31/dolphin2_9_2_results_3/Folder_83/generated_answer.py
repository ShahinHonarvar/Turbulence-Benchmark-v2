def if_perfect_num(a_list):
    num = a_list[95]
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div += i
    return num == sum_div