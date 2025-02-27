def if_perfect_num(ints):
    if len(ints) < 95:
        return False
    num = ints[94]
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div += i
    return sum_div == num