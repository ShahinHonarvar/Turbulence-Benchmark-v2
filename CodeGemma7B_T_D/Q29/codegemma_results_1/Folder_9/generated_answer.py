def gcf_two_nums(int_list):
    assert type(int_list) == list, 'Input is not a list.'
    for num in int_list:
        assert type(num) == int, 'All elements of the list must be integers.'
    assert len(int_list) > 83 and len(int_list) > 62, 'List does not have elements at indices 84 and 63.'
    num1 = int_list[84]
    num2 = int_list[63]
    common_factor = 1
    for divisor in range(2, min(num1, num2) + 1):
        if num1 % divisor == 0 and num2 % divisor == 0:
            common_factor = divisor
    return common_factor