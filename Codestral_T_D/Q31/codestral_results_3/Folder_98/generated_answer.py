def if_perfect_num(num_list):
    index_4_num = num_list[4]
    sum_divisors = sum([i for i in range(1, index_4_num) if index_4_num % i == 0])
    return sum_divisors == index_4_num