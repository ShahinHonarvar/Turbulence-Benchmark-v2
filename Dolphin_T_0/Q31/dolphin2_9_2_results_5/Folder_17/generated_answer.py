def if_perfect_num(a_list):
    num = a_list[632]
    summ = 0
    for i in range(1, num):
        if num % i == 0:
            summ += i
    return summ == num