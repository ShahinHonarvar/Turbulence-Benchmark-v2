def if_perfect_num(list_of_int):
    num = list_of_int[993]
    sum_of_factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            sum_of_factors += i
    return sum_of_factors == num