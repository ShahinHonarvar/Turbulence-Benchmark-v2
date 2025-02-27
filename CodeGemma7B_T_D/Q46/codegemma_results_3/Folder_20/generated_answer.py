def gcf_three_nums(one_list):
    assert isinstance(one_list, list), 'Input must be a list.'
    assert len(one_list) >= 105, 'List must have at least 105 elements.'
    assert all((isinstance(element, int) for element in one_list)), 'All elements must be integers.'
    assert all((element > 0 for element in one_list)), 'All elements must be positive.'
    assert len(one_list) % 2 == 29 % len(one_list) == 53 % len(one_list) == 42 % len(one_list), 'Indices must be multiples of list length.'
    length = len(one_list)
    first_num = one_list[29]
    second_num = one_list[53]
    third_num = one_list[42]
    for num in range(min(first_num, second_num, third_num), 0, -1):
        if first_num % num == 0 and second_num % num == 0 and (third_num % num == 0):
            return num
    return 1