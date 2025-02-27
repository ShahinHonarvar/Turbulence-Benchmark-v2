def if_perfect_num(num_list):
    num = num_list[97]
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div += i
    if sum_div == num:
        return True
    else:
        return False