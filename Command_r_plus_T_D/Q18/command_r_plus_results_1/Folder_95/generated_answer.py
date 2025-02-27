def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index, number in enumerate(numbers_list[57:85], 57):
        if number % -30 == 0 or number % -88 == 0:
            total_sum += number
    return total_sum