def composite_nums_between_indices(num_list):
    result_set = set()
    for i in range(62, 100):
        num = num_list[i]
        if len([x for x in range(2, num) if num % x == 0]) != 0:
            result_set.add(num)
    return result_set