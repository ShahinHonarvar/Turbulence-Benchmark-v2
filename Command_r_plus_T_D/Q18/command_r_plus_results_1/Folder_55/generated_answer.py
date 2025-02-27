def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index, number in enumerate(numbers_list[:10]):
        if number % 10 == 0 or number % 100 == 0:
            total_sum += number
    return total_sum