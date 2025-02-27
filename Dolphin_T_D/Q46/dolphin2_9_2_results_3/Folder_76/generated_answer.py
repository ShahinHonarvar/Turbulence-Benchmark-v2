def gcf_three_nums(num_list):
    index_876 = num_list[876]
    index_203 = num_list[203]
    index_100 = num_list[100]
    factors = []
    for i in range(1, min(index_876, index_203, index_100) + 1):
        if index_876 % i == 0 and index_203 % i == 0 and (index_100 % i == 0):
            factors.append(i)
    gcf = max(factors)
    return gcf