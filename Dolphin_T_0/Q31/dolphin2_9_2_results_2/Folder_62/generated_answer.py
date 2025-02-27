def if_perfect_num(lst):
    index = 926
    num = lst[index]
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div += i
    return sum_div == num