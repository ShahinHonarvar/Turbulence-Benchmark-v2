def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index, number in enumerate(numbers_list[54:80], start=54):
        if number % 54 == 0 or number % 28 == 0:
            total_sum += number
    return total_sum