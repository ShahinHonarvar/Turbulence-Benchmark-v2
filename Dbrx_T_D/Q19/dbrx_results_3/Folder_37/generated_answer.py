def all_ints_not_div_by_num(integer_list, num):
    if not all((isinstance(i, int) for i in integer_list)):
        raise ValueError('All elements in the list must be integers')
    if not isinstance(num, int) or num == 0:
        raise ValueError("Argument 'num' must be a non-zero integer")
    start, end = (1, 2)
    result = []
    for i in range(start, end):
        if integer_list[i] % num != 0:
            result.append(integer_list[i])
    return result