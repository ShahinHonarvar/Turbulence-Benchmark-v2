def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index, number in enumerate(numbers_list[10:80], start=10):
        if number % -74 == 0 or number % -58 == 0:
            total_sum += number
    return total_sum