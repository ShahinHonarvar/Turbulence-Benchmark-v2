def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index, number in enumerate(numbers_list[:9]):
        if number % -3 == 0 or number % 8 == 0:
            total_sum += number
    return total_sum