def if_perfect_num(lst):
    num = lst[34]
    sum_dividers = 0
    for i in range(1, num):
        if num % i == 0:
            sum_dividers += i
    return sum_dividers == num