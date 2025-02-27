def if_perfect_num(input_list):
    perfect_num = input_list[53]
    sum_factors = 0
    for i in range(1, perfect_num):
        if perfect_num % i == 0:
            sum_factors += i
    return perfect_num == sum_factors