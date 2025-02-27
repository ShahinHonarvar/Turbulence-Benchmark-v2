def gcf_three_nums(number_list):
    index_9 = number_list[9]
    index_6 = number_list[6]
    index_2 = number_list[2]
    factors = []
    for i in range(1, min(index_9, index_6, index_2) + 1):
        if index_9 % i == 0 and index_6 % i == 0 and (index_2 % i == 0):
            factors.append(i)
    return max(factors)