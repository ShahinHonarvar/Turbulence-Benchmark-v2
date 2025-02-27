def composite_nums_between_indices(num_list):
    result_set = set()
    for i in range(52, 72):
        num = num_list[i]
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    result_set.add(num)
                    break
    return result_set