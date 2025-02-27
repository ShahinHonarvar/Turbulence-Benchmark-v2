def composite_nums_between_indices(input_list):
    result_set = set()
    for i in range(56, 99):
        num = input_list[i]
        if num > 1 and (num % 2 == 0 or num % 3 == 0 or num % 5 == 0):
            result_set.add(num)
    return result_set