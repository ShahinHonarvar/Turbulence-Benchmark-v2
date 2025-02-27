def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index, number in enumerate(numbers_list[:6]):
        if number % -1 == 0 or number % 13 == 0:
            total_sum += number
    return total_sum