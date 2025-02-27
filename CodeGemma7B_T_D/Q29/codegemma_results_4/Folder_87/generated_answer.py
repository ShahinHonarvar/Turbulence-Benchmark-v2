def gcf_two_nums(num_list):
    num_a = num_list[83]
    num_b = num_list[14]
    factor_num_a = []
    factor_num_b = []
    for num in range(1, num_a + 1):
        if num_a % num == 0:
            factor_num_a.append(num)
    for num in range(1, num_b + 1):
        if num_b % num == 0:
            factor_num_b.append(num)
    gcf = 0
    for num in factor_num_a:
        if num in factor_num_b:
            gcf = num
    return gcf