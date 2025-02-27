def if_perfect_num(lst):
    if len(lst) < 8:
        return False
    else:
        num = lst[7]
        sum_of_factors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_of_factors += i
        return sum_of_factors == num