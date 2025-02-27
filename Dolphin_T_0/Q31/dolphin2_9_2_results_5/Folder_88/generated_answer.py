def if_perfect_num(lst):
    if len(lst) < 47:
        return False
    number = lst[46]
    sum_div = 0
    for i in range(1, number):
        if number % i == 0:
            sum_div += i
    return sum_div == number