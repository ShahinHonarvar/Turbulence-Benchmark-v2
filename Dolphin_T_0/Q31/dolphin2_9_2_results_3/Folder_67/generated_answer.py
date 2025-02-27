def if_perfect_num(input_list):
    number = input_list[43]
    sum_factors = 1
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            sum_factors += i
    return sum_factors == number