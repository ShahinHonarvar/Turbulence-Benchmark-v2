def if_perfect_num(lst):
    if len(lst) < 73:
        return False
    num = lst[72]
    sum_de = 1
    for i in range(2, num):
        if num % i == 0:
            sum_de += i
    if sum_de == num:
        return True
    else:
        return False