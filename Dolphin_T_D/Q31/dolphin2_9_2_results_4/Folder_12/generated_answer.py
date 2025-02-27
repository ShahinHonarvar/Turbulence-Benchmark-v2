def if_perfect_num(lst):
    num = lst[27]
    factors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            factors_sum += i
    return factors_sum == num