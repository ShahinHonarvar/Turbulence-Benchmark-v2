def gcf_three_nums(lst):
    num_1, num_2, num_3 = (lst[14], lst[21], lst[17])
    factor_list = []
    for num in (num_1, num_2, num_3):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                factor_list.extend([i, num // i])
    max_factor = max(set(factor_list))
    return max_factor